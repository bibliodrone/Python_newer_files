# import xml.etree.ElementTree as ET
import urllib.request

url = ('http://lms01.harvard.edu/EDI_Invoices/edi_logs_report.html')

data = urllib.request.urlopen(url).read()

for item in data:
    print (item)

