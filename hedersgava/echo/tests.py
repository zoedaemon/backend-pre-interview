"""
echo api testing
"""
from string import printable
from datetime import datetime
import pytest
#import json
from hypothesis import strategies as st
#from hypothesis import given, example
#from hypothesis.extra.django import register_field_strategy
from hypothesis.extra.django import from_model
from hypothesis.strategies import just

#from django.test import Client
from .views import echo_filter#, echo
from .models import DeviceType, DeviceRecords

JSON_DATA = st.recursive(st.booleans() | st.floats() | st.text(printable),
                         lambda children: st.dictionaries(st.text(printable), children))

class TestEcho:
    """
    TestEcho class testers
    """
    #@given(json_data=JSON_DATA)
    #@example('')
    @pytest.mark.django_db
    def test_echo_json_status_result(self, rf): # pylint: disable=invalid-name
        """
        Testing echo api response status result is function correctly with json data
        """
        #data = {'null':json.dumps(json_data)}
        #dt = from_model(DeviceType).example()
        #set manual foreign key dt.id
        #dr = from_model(DeviceRecords, devices_type=just(dt.id)).example()
        #strategy = register_field_strategy(DeviceType, DeviceType(id=1, name="voltage", unit="V"))
        #dr = from_model(DeviceRecords, devices_type=from_model(DeviceType)).example()
        device_type = from_model(DeviceType, id=just(1))
        device_records = from_model(DeviceRecords, devices_type=device_type).example()
        request = rf.get('data/'+str(datetime.timestamp(device_records.record_time))+'/',
                         None, content_type='application/json')
        response = echo_filter(request, int(datetime.timestamp(device_records.record_time)))
        assert response.status_code == 200
        response.render()
        #assert response.data == data
