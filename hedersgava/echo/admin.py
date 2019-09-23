"""
import models admin here
"""
from django.contrib import admin

# Register your models here.
from .models import DeviceType, DeviceTypeAdmin
from .models import DeviceRecords, DeviceRecordsAdmin

admin.site.register(DeviceType, DeviceTypeAdmin)
admin.site.register(DeviceRecords, DeviceRecordsAdmin)
