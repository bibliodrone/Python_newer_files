#! python3
# quickWeather.py - Prints the weather for a location from the command line.
# From 'Automate the Boring Stuff with Python' (Sweigart)

import json, requests, sys
from pprint import pprint
"""
# Compute location from command line arguments.
if len(sys.argv) < 2:
    print('Usage: quickWeather.py location')
    sys.exit()
location = ' '.join(sys.argv[1:])
"""

url =('http://webservices.lib.harvard.edu/rest/v2/classic/holdings/001252867?jsonp=ws_results')

'''
struct = {}
try:
  try: #try parsing to dict
    dataform = str(response_json).strip("'<>() ").replace('\'', '\"')
    struct = json.loads(dataform)
  except:
    print repr(resonse_json)
    print sys.exc_info()
'''    
# Download the JSON data 
response = requests.get(url).json()
response.raise_for_status()
print (response.text())

'''Load JSON data into a Python variable.
bibData = json.loads(response.text)
pprint(bibData)
Print weather descriptions.
'''
'''
print(b[0]['results'])

print()
print('Tomorrow:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('Day after tomorrow:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])
'''
