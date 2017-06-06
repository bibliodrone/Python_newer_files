#readexml.py
#Make some sense of an ERIN xml export.
#using Record_Load_History.xml

from __future__ import print_function
from bs4 import BeautifulSoup
import csv


w = open("ERIN_result.csv", "w", newline='')

#print("csv file open failed")

outWriter = csv.writer(w)

with open('Record_Load_History.xml', 'r') as f:
    
    soup = BeautifulSoup(f, 'html.parser')

    r_request = soup.find_all('related_request')
    desc = soup.find_all('title')
    library = soup.find_all('library')

    print("REQ    LIB")

    for i in range(len(r_request)):
        x = r_request[i].get_text()
        y = desc[i].get_text().encode()
        z = library[i].get_text()
        
        outWriter.writerow([x, y.decode('utf-8'), z])

print ('Process completed. File is \"ERIN_Result.csv\".')

#print(request)
#print(lib)

f.close()
w.close()

