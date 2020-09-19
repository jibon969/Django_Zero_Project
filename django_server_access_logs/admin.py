from django.contrib import admin
from .models import AccessLogsModel
# Register your models here.


class AccessLogsModelAdmin(admin.ModelAdmin):
    list_display = ['sys_id', 'session_key', 'ip_address', 'path']
    list_per_page = 20

    class Meta:
        model = AccessLogsModel


admin.site.register(AccessLogsModel, AccessLogsModelAdmin)