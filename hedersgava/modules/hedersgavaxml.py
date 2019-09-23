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
import xml.etree.ElementTree as ET 

class XMLParser(object):
    """
       class custom parser for Hedersgåva input requirements
    """
    @staticmethod
    def parse(xml_data):
        # create element tree object 
        tree = ET.ElementTree(ET.fromstring(xml_data)) 
        #print (xml_data)
        # get root element 
        root = tree.getroot()
        # create empty list for news items 
        elements = [] 
        # iterate throught element 
        for elem in root.findall('./data/element'):
            # iterate child elements of item 
            for child in elem: 
                print (child.text.encode('utf8'))