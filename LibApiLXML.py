import requests
import lxml 

r=requests.get('http://webservices.lib.harvard.edu/rest/v2/classic/holdings/001252867')
path = r
parsed = lxml.objectify.parse(open(path))
root = parsed.getroot()
