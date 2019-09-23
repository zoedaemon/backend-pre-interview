"""
Hedersgåva models, consist of :
1) DeviceType
2) DeviceTypeAdmin
"""
from django.db import models
from django.contrib import admin

class DeviceType(models.Model):
    """
        model of device type (e.g. Temperature Sensor, Voltage Meter, etc)
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    unit = models.CharField(max_length=20)
    #def __str__(self):
    #    return self.name

class DeviceTypeAdmin(admin.ModelAdmin):
    """
        model DeviceType for admin use
    """
    list_display = ('id', 'name', 'unit')
