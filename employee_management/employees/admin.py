from django.contrib import admin
from django.utils.html import format_html
from .models import Employee

## employees admin code
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'position', 'department', 'get_status', 'get_action_buttons')
    list_filter = ('status', 'department', 'created_at')
    search_fields = ('full_name', 'email', 'position', 'department')
    readonly_fields = ('created_by', 'created_at', 'updated_at')
    change_list_template = "admin/employees/change_list.html"

    def get_status(self, obj):
        if obj.status == 'PENDING':
            return format_html(
                '<span style="background-color: #FFA500; color: white; padding: 5px; '
                'border-radius: 5px;">{}</span>',
                obj.get_status_display()
            )
        return format_html(
            '<span style="background-color: #28a745; color: white; padding: 5px; '
                'border-radius: 5px;">{}</span>',
            obj.get_status_display()
        )
    get_status.short_description = 'Status'

    def get_action_buttons(self, obj):
        if obj.status == 'PENDING':
            return format_html(
                '<div class="button-container">'
                '<a class="button" style="background-color: #007bff; color: white; '
                'padding: 5px 10px; border-radius: 5px; margin-right: 5px; '
                'text-decoration: none;" href="{}">Edit</a>'
                '<a class="button" style="background-color: #28a745; color: white; '
                'padding: 5px 10px; border-radius: 5px; margin-right: 5px; '
                'text-decoration: none;" href="{}">Verify</a>'
                '<a class="button" style="background-color: #dc3545; color: white; '
                'padding: 5px 10px; border-radius: 5px; text-decoration: none;" '
                'href="{}">Delete</a>'
                '</div>',
                f'/admin/employees/employee/{obj.id}/change/',
                f'/api/employees/{obj.id}/verify/',
                f'/admin/employees/employee/{obj.id}/delete/'
            )
        return format_html(
            '<span style="color: #28a745; font-weight: bold;">✓ Verified</span>'
        )
    get_action_buttons.short_description = 'Actions'
# custom css fro admin
    class Media:
        css = {
            'all': ('admin/css/custom_admin.css',)
        }