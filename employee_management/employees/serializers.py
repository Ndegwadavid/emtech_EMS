from rest_framework import serializers
from .models import Employee
import re

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
        read_only_fields = ('created_by', 'created_at', 'updated_at')

    def validate_phone_number(self, value):
        # phne number validation
        if not re.match(r'^\+?1?\d{9,15}$', value):
            raise serializers.ValidationError(
                "Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
            )
        return value

    def validate_email(self, value):
        # Check if email is unique
        if Employee.objects.filter(email=value).exists():
            raise serializers.ValidationError("An employee with this email already exists.")
        return value

    def validate(self, data):
        if 'position' in data and 'department' in data:
            if data['department'].lower() == 'it' and not any(
                tech in data['position'].lower() 
                for tech in ['developer', 'engineer', 'analyst', 'administrator']
            ):
                raise serializers.ValidationError(
                    "Position doesn't match IT department conventions"
                )
        return data
    
    