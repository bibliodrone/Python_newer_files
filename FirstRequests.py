import urllib.request
import xml.etree.ElementTree as ET

url = 'http://webservices.lib.harvard.edu/rest/cite/hollis/011557057'
Library = urllib.request.urlopen(url)
data = Library.read()
tree=ET.fromstring(data)

Treelist=tree.findall('//')


for elem in Treelist:
    print (str(elem))


