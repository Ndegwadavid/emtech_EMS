from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.core.exceptions import ValidationError
from django.db.models import Q
from .models import Employee
from .serializers import EmployeeSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        queryset = Employee.objects.all()
        
        # filtering by status,  verified or not verified
        status = self.request.query_params.get('status', None)
        if status:
            queryset = queryset.filter(status=status.upper())
        
        # Search functionality for an employee either by regustered params
        search = self.request.query_params.get('search', None)
        if search:
            queryset = queryset.filter(
                Q(full_name__icontains=search) |
                Q(email__icontains=search) |
                Q(position__icontains=search) |
                Q(department__icontains=search)
            )
        
        # filtering based on department
        department = self.request.query_params.get('department', None)
        if department:
            queryset = queryset.filter(department__iexact=department)
            
        return queryset.order_by('-created_at')

    def create(self, request, *args, **kwargs):
        try:
            # add to reqiest data cretaed by who?
            request.data['created_by'] = request.user.id
            return super().create(request, *args, **kwargs)
        except ValidationError as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )

    def update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            if instance.status == 'VERIFIED':
                return Response(
                    {'error': 'Verified employees cannot be modified'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            return super().update(request, *args, **kwargs)
        except ValidationError as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )

    @action(detail=True, methods=['post'])
    def verify(self, request, pk=None):
        try:
            employee = self.get_object()
            if employee.status == 'VERIFIED':
                return Response(
                    {'error': 'Employee is already verified'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            employee.status = 'VERIFIED'
            employee.save()
            serializer = self.get_serializer(employee)
            return Response(serializer.data)
        except Exception as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )

    @action(detail=False, methods=['get'])
    def statistics(self, request):
        total_employees = Employee.objects.count()
        verified_count = Employee.objects.filter(status='VERIFIED').count()
        pending_count = Employee.objects.filter(status='PENDING').count()
        
        return Response({
            'total_employees': total_employees,
            'verified_employees': verified_count,
            'pending_employees': pending_count,
            'verification_rate': f"{(verified_count/total_employees)*100:.2f}%" if total_employees > 0 else "0%"
        })