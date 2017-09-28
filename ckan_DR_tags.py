import requests
import json


url = 'https://www.datarefuge.org/api/3/action/tag_list'

# Request a package list.
response = requests.get(url)
response.raise_for_status

manifest = json.loads(response.text)
#pprint.pprint(response)
ml = manifest['result']

with open('data_refuge_tags.txt', 'w', encoding = 'utf-8') as outfile:
    outfile.write('List of tags (uncontrolled) on Data Refuge\n\n')
    for m in ml:
        outfile.write(str(m)+"\n")

