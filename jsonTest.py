import json
import urllib.request
from pprint import pprint

def ws_results(connection):
    js =(connection.read())
    parsed_js = json.loads(js.decode())

    print(parsed_js['collectionname'])

    
ws_results(connection = urllib.request.urlopen('http://webservices.lib.harvard.edu/rest/v2/classic/holdings/014472259/brief?jsonp=ws_results'))
