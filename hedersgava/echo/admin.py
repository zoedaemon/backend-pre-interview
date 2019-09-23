"""
import models admin here
"""
from django.contrib import admin

# Register your models here.
from .models import DeviceType, DeviceTypeAdmin
admin.site.register(DeviceType, DeviceTypeAdmin)
