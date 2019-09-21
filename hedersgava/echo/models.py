from django.db import models
from django.contrib import admin

# Create your models here.
class DeviceType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    unit = models.CharField(max_length=20)
    #def __str__(self):
    #    return self.name

class DeviceTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'unit')    
