"""
Hedersgåva serializers
"""
from rest_framework import serializers
from .models import DeviceType, DeviceRecords

class DeviceTypeSerializer(serializers.ModelSerializer):
    """
    json serializers for DeviceType
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=False, allow_blank=True, max_length=100)
    unit = serializers.CharField(required=False, allow_blank=True, max_length=20)
    def get(self, validated_data):
        #Create and return a instance, given the validated data.
        return DeviceType.objects.get(**validated_data)
    """
    class Meta:
        model = DeviceType
        fields = ['id', 'name', 'unit']
    def __str__(self):
        return self.name # pylint: disable=no-member

class DeviceRecordsSerializer(serializers.ModelSerializer):
    """
    json serializers for DeviceRecords
    """
    #owner = PrimaryKeyRelatedField(queryset=User.objects.all())
    class Meta:
        model = DeviceRecords
        fields = ['record_time', 'id_input', 'devices_id', 'devices_type',
                  'value']
