from django.db import models

# Create your models here.
class DeviceType(models.Model):
    name = models.CharField(max_length=100)
    unit = models.CharField(max_length=20)