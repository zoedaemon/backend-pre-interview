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
    def __str__(self):
        return self.name + " (" + self.unit + ")"

class DeviceTypeAdmin(admin.ModelAdmin):
    """
        model DeviceType for admin use
    """
    list_display = ('id', 'name', 'unit')

class DeviceRecords(models.Model):
    """
        model that store device records
        record_time : hold timestamp described in input file (xml)
        ...
        TODO:devices_id & devices_type can set to independent model
        TODO:on_delete=CASCADE, need to be revised see :
             https://stackoverflow.com/questions/2475249/what-are-the-options-for
             -overriding-djangos-cascading-delete-behaviour
    """
    record_time = models.DateTimeField()
    id_input = models.IntegerField()
    devices_id = models.CharField(max_length=100)
    devices_type = models.OneToOneField(DeviceType,
                                        on_delete=models.CASCADE,
                                        primary_key=False)
    value = models.DecimalField(max_digits=7, decimal_places=3)

class DeviceRecordsAdmin(admin.ModelAdmin):
    """
        model DeviceRecords for admin use
    """
    list_display = ('record_time', 'id_input', 'devices_id', 'devices_type',
                    'value')
