from django.contrib import admin
from .models import Enterprise

# Register your models here.
class EnterpriseAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')
    list_display_links = ('name', 'email')
    ordering = ('-id',)
    filter_horizontal = ()
    list_filter = ()

admin.site.register(Enterprise, EnterpriseAdmin)