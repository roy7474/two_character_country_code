'''
Exercise 1: Change either geojson.py or geoxml.py to:
1) print out the two- character country code from the retrieved data.
2) Add error checking so your program does not traceback if the country code is not there.
3) Once you have it working, search for “Atlantic Ocean” and make sure it can handle 
   locations that are not in any country.
'''

# program chosen: geoxml.py

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

