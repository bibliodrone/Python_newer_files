import xml.etree.ElementTree as ET
import urllib.request

url = ('http://webservices.lib.harvard.edu/rest/v2/classic/holdings/001252867')

data = urllib.request.urlopen(url).read()
 
availability = ET.fromstring(data)

allLines = tree.findall('//')

for item in allLines :
    print (item.findall().text)