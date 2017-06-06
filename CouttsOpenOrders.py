#From ISBN list file, get HOLLIS record ID's
#Expects: ...isbnsearchlist.txt
#Returns: csv file ...ResultsFile.csv

#if using python 2.x: from __future__ import print_function

from bs4 import BeautifulSoup
import urllib.request
import csv

try:
    file = open("CouttsResultsFile.csv", "w", newline = '')
except:
    print("Could not create resultsFile")

outWriter = csv.writer(file)
with open('coutts_isbnsearchlist.txt', 'r') as f:
    for line in f:
        url =('http://webservices.lib.harvard.edu/rest/mods/hollis/isbn/'+ line)

        isbn = str(line).rstrip()

        try: 
            data=urllib.request.urlopen(url).read()
        except:
            continue

        soup = BeautifulSoup(data, 'html.parser')

        #Variables: location, recID--> BibNo, hols 
        location = soup.find_all('physicallocation')
        recID = soup.find_all('recordidentifier')
        title = soup.find_all('title')
        place = soup.find_all('placeTerm')
        change = soup.find_all ('recordChangeDate')

        physlc = []
        for item in (location)
            physlc.append(item.get_text())
            
        BibNo = []
        for item in(recID):
            BibNo.append(item.get_text())

        titl = []
        for item in (title):
            titl.append(item.get_text())
    
        plc = []
        for item in (place):
            plc.append(item.get_text())
            
        chdt = []
        for item in (change):
            chdt.append(item.get_text())

        outWriter.writerow([isbn, BibNo, hols])
        print("ISBN: ",str(isbn)," BibNo. ", str(BibNo)," Holdings ", str(hols))

        print("*")

print("Search Complete. File is", file)
  
file.close()
