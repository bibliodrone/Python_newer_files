# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 20:41:05 2017
Search Library of Congress for an ISBN, and get the permalink in return
@author: walden
"""

import requests, bs4

defaultibn = "9781593275990"
isbn = defaultibn

isbn=input("Scan in an ISBN ->> ")



url = "https://catalog.loc.gov/vwebv/search?searchArg="+isbn+"&searchCode=KNUM&searchType=0&recCount=25"

print("Searching", isbn)

response = requests.get(url)
response.raise_for_status()

record = bs4.BeautifulSoup(response.text, "lxml")
tag = record.select("#permalink")
    
perma = str(tag[0].getText())
    
print("Permalink result: ", perma)


url2 = perma+"/mods"


response2 = requests.get(url2)
response2.raise_for_status()

record2 = bs4.BeautifulSoup(response2.text, "lxml")
tag2 = record2.select("classification[authority]")

ln = len(tag2)

for i in range (0, ln):
    print(str(tag2[i].getText()))
    