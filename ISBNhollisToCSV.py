from __future__ import print_function
from bs4 import BeautifulSoup
import urllib.request
import csv

try:
    file = open("resultsFile.csv", "w", newline = '')
except:
    print("Could not create resultsFile")

outWriter = csv.writer(file)
with open('isbnsearchlist.txt', 'r') as f:
    for line in f:
        url =('http://webservices.lib.harvard.edu/rest/mods/hollis/isbn/'+ line)

        isbn = str(line).rstrip()

        try: 
            data=urllib.request.urlopen(url).read()
        except:
            continue

        soup = BeautifulSoup(data, 'html.parser')

        #Variables: location, recID--> BibNo, hols
        tags=soup.find_all()
        for t in tags:
            print (t)
"""
        location = soup.find_all('physicallocation')
        recID = soup.find_all('recordidentifier')
        BibNo = []
        for item in(recID):
            BibNo.append(item.get_text())

        hols=[]
        for item in (location):
            hols.append(item.get_text())

        outWriter.writerow([isbn, BibNo, hols])
        print("ISBN: ",str(isbn)," BibNo. ", str(BibNo)," Holdings ", str(hols))

        print("*")

print('Search Complete. File is \"resultsFile.csv\".')
"""
file.close()
