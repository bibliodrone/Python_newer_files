
#jsonUrl.py

import requests
import json

url = "http://webservices.lib.harvard.edu/rest/v2/classic/holdings/014472259/brief?jsonp=results"
reply = json.loads(url)

for entry in reply['items']['itemrecord']:
    print (entry['barcode'])
