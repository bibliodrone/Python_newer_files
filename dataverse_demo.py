#dataverse-demo.py

import requests 
import json
#base = 'https://demo.dataverse.org'
base = 'https://www.datarefuge.org'

rows = 10
start = 0
page = 1
condition = True # emulate do-while
while (condition):
    url = base + '/api/search?q=weather' + '&res_format=JSON'
    data = requests.get(url)
    data.raise_for_status()
    data = json.loads(data.text)
    #total = data['data']['total_count']
    total = 3
    print ("=== Page", page, "===")
    print ("start:", start, " total:", total)
    for i in data['data']['items']:
        print ("- ", i['name'], "(" + i['type'] + ")")
    start = start + rows
    page += 1
    condition = start < total
