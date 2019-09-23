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
from collections import defaultdict

class XMLParser(object):#pylint: disable=useless-object-inheritance
    """
       class custom parser for Hedersgåva input requirements
    """
    @staticmethod
    def parse(xml_data):
        """
           parse function to read xml data
        """
        # create element tree object
        tree = ET.ElementTree(ET.fromstring(xml_data))
        #print (xml_data)
        # get root element
        root = tree.getroot()
        # create empty list for news items
        elements = defaultdict(list)
        # iterate throught element
        #TODO: exception handling if invalid element
        for elem in root.findall('./data/element'):
            # iterate child elements of item
            for child in elem:
                if child.tag == "device":
                    #hold for elements key
                    device = child.text
                    #print (device)
                elif child.tag == "value":
                    #save to elements
                    elements[device] = child.text#.encode('utf8')
                    #print (elements[device])
                #else:
                #    None# TODO : raise error
        #check items in elements
        #for k,v in elements.items():
            #for value in v:
                #print(f'{k}')
        # reset to root element
        #root = tree.getroot()
        for elem in root.findall('./devices'):
            for child in elem:
                if elements[child.tag] is not None:
                    print(elements[child.tag])
