import requests
from lxml import objectify, etree
from io import StringIO, BytesIO

r=requests.get('http://webservices.lib.harvard.edu/rest/v2/classic/holdings/001252867')
f=open("questor.txt", 'a')
    for line in r:
        f.write(line)
        
f.close()
