import requests
from bs4 import BeautifulSoup

r=requests.get('http://webservices.lib.harvard.edu/rest/classic/results/dc/937338/1000/26/50?wrd=physics')

soup = BeautifulSoup(r)

collection = soup.find_all('results')

print (collection)
'''
r
'''
