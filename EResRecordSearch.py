from bs4 import BeautifulSoup
import urllib.request
import time
import re
import csv

isn_list = []
result_list = []
try:
    with open('isn_short_list.txt', 'r') as isns:
        for i in isns:
            j = i.strip()
            isn_list.append(j)
except IOError:
    print("Could not open isn text file")

for n in isn_list:
    
    url=('http://webservices.lib.harvard.edu/rest/classic/search/mods/isn=' + n)

    print("\nSearching", n)

    try:
        data=urllib.request.urlopen(url).read()

        soup = BeautifulSoup(data, "html.parser")
        li = soup("physicallocation")
        ri = soup("recordidentifier")
        ur = soup("url")
        if len(ri)>0:
            print ("Record found", end = ": ")
            for r in ri:
                print (r.get_text())
                result_list.append('\n' + r.get_text())
            for e in li:
                print(e.get_text())
                result_list.append(e.get_text())
            for u in ur:
                print(u.get_text())
                result_list.append(u.get_text())
    
    except: print("No data returned")            

    time.sleep(1)

print("Run completed")

with open ('isn_results.txt', 'w') as w:
    for item in result_list:
        w.write(item + '\n')
        
print("isn_results.txt --> created.")
"""
li = soup("physicallocation")

>>>for e in li:
	print(e)

<physicallocation>NET</physicallocation>
<physicallocation>CAB</physicallocation>
<physicallocation>FIG</physicallocation>

>>> for e in li:
	print(e.get_text())

NET
CAB
FIG

"""
