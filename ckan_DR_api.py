#!/usr/bin/env python

# ckan_api.py -- CKAN sample
# Data Refuge's API:
#   https://www.datarefuge.org/api/3 
#   sample url: https://www.datarefuge.org/api/3/action/package_list
#   note the use of 'help', 'success', 'result' as labels within the json page,
#   which this program is primed to look for. 

import requests
import json


url = 'https://www.datarefuge.org/api/3/action/package_list'

# Request a package list.
response = requests.get(url)
response.raise_for_status

manifest = json.loads(response.text)
#pprint.pprint(response)
ml = manifest['result']

with open('data_refuge_packages.txt', 'w', encoding = 'utf-8') as outfile:
    outfile.write('List of packages on Data Refuge\n\n')
    for m in ml:
        outfile.write(str(m)+"\n")



      
"""
# Use the json module to load CKAN's response into a dictionary.
response_dict = json.loads(response.read())
assert response_dict['success'] is True

# package_create returns the created package as its result.
created_package = response_dict['result']
pprint.pprint(created_package)
"""
