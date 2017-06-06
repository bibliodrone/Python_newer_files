#hollisGetParse.py
#Input: text file of ISBN's
#Output: csv file of corresponding holdings and title info, if in HOLLIS

from __future__ import print_function
from bs4 import BeautifulSoup
import urllib.request
import time
import re
import csv

#One way to create unique filenames: append int(time.time())
#holdings = []

try:
    fh = open("resultsFile.csv", "w", newline = '')
except:
    print("Could not create resultsFile")

outWriter = csv.writer(fh)
with open('isbnsearchlist.txt', 'r') as f:
    for line in f:
        url =('http://webservices.lib.harvard.edu/rest/mods/hollis/isbn/'+ line)
        #print("/nISBN " + line + " : ", file=fh)
        #record=[]
        ls = str(line).rstrip()
        #record.append(str(line))
        try: 
            data=urllib.request.urlopen(url).read()
        except:
            #print("not found", file=fh)
            print("NONE, NONE,,")

            #print("\/", end = "")
            #record.append("not found")
            continue
        
        soup = BeautifulSoup(data, "html.parser")
        physLoc = soup.find_all('physicallocation')
        recID = soup.find_all('recordidentifier')
        
        #print("Sys no.: " + recID[0].get_text(), end = ":: ", file=fh)
        rs=str(recID[0].get_text())
        #print(rs, end=", ")
        #record.append(recID[0].get_text())
        #print("  >>Holdings", end=": ")
        phLoc=[""]
        for item in (physLoc):
            #print("HOL "+ item.get_text(), end = " ; ", file=fh)
            phLoc.append(item.get_text())
            #print(pl, end = ", ")
            #holdings.append(str(item.get_text))
        print(",,")
        #print("\/", end="")
        #holdings.append(record)
        time.sleep(0.3)

print("\nSearch completed. Have a nice day...")

fh.close

#except IOError:
#    print("Cannot find ISBN File.")
#except SyntaxError:
#    print("There was a problem with the website's response")
#else:
#    print("Program ran successfully")
