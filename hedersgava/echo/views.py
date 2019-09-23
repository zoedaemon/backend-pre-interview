"""
Hedersgåva views
"""
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response as response
from .models import DeviceType
from .serializers import DeviceTypeSerializer
from modules import HedersgavaXMLParser

@api_view(['POST'])
def echo(request):
    """
    Request json data and return it
    """
    if request.method == 'GET':
        #serialize = DeviceTypeSerializer( DeviceType.objects.get(unit='V') )
        dtset = DeviceType.objects.all()
        serialize = DeviceTypeSerializer(dtset, many=True)
        if serialize:
            HedersgavaXMLParser.parse('olla')
            return response(serialize.data, status=200, content_type=request.content_type)
        return response(status=status.HTTP_400_BAD_REQUEST)
    return None
