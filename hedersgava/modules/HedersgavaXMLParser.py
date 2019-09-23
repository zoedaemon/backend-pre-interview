"""
Hedersgåva xml parser; valid input format : 
*** Please see .models/DeviceRecords ***
<?xml version="1.0" encoding="UTF-8"?>
<root>
   <data>
      <element>
         <device> DEVICE_ID </device>
         <value> VALUE </value>
      </element>
      ...
   </data>
   <devices>
      <DEVICE_ID> DEVICE_TYPE </DEVICE_ID>
      ...
   </devices>
   <id> ID_INPUT </id>
   <record_time> RECORD_TIME </record_time>
</root>
"""
class HedersgavaXMLParser(object):
    """
       class custom parser for Hedersgåva input requirements
    """
    @staticmethod
    def parse(xml_data):
        print ("imported")
