
from django.contrib import admin
from .models import Employee

#employees admin code

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'position', 'department', 'status', 'created_at')
    list_filter = ('status', 'department', 'created_at')
    search_fields = ('full_name', 'email', 'position')
    readonly_fields = ('created_by', 'created_at', 'updated_at')
    
    def save_model(self, request, obj, form, change):
        if not change:  # If creating new employee
            obj.created_by = request.user
        super().save_model(request, obj, form, change)

