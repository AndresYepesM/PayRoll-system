from django.contrib import admin
from .models import Enterprise, Employee, Position

# Register your models here.
class EnterpriseAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')
    list_display_links = ('name', 'email')
    ordering = ('-id',)
    filter_horizontal = ()
    list_filter = ()

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'enterprise','phone')
    list_display_links = ('full_name', 'email')
    ordering = ('-id',)
    filter_horizontal = ()
    list_filter = ()

class PositionAdmin(admin.ModelAdmin):
    list_display = ('name', 'enterprise')

admin.site.register(Enterprise, EnterpriseAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Position, PositionAdmin)