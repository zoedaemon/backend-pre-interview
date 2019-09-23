"""
Hedersgåva views
"""
from datetime import datetime
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response as response
import pytz
from modules import hedersgavaxml
from .models import DeviceType, DeviceRecords
from .serializers import DeviceTypeSerializer, DeviceRecordsSerializer

@api_view(['POST'])
def echo(request):
    """
    Request json data and return it
    """
    if request.method == 'POST':
        #serialize = DeviceTypeSerializer( DeviceType.objects.get(unit='V') )
        dtset = DeviceType.objects.all()
        serialize = DeviceTypeSerializer(dtset, many=True)
        if serialize:
            hedersgavaxml.XMLParser.parse(request.body)
            return response(serialize.data, status=200, content_type=request.content_type)
        return response(status=status.HTTP_400_BAD_REQUEST)
    return None

@api_view(['GET'])
def echo_filter(request, filter_timestamp):
    #Request json data and return it
    """
    echo views : converting timestamp as url parameter to datetime
    """
    if request.method == 'GET':
        #tzname = request.session.get('django_timezone')
        #local_tz = pytz.timezone(timezone.now())
        local_tz = pytz.timezone('Asia/Jakarta')
        utc_dt = datetime.utcfromtimestamp(filter_timestamp).replace(tzinfo=pytz.utc)
        dt_value = local_tz.normalize(utc_dt.astimezone(local_tz))
        dt_value = dt_value.strftime('%Y-%m-%dT%H:%M:%SZ')
        print(dt_value)
        #TODO: exception handling if objects not found
        dtset = DeviceRecords.objects.filter(record_time=dt_value)#.union()
        #dtset = DeviceRecords.objects.all()
        serialize = DeviceRecordsSerializer(dtset, many=True)
        if serialize:
            hedersgavaxml.XMLParser.parse('olla')
            return response(serialize.data, status=200, content_type=request.content_type)
        return response(status=status.HTTP_400_BAD_REQUEST)
    return None
