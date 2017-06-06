#fdlpDups.py
#Next phase would be to return title, isbn, holdings etc. from Hollis

from __future__ import print_function
from bs4 import BeautifulSoup
import urllib.request
import time
import re

def getReport(link_full):
    try:
        newData = urllib.request.urlopen(link_full).read()
        soup = BeautifulSoup(newData, "html.parser")
        report = soup.get_text()
        print (report)
    except:
        print ("There was a problem getting the report")


url = ('https://lms01.harvard.edu/ebooks/fdlp/')
pattern = re.compile("^.*mult.*$")
logList=[]

try: 
    data=urllib.request.urlopen(url).read()
    soup = BeautifulSoup(data, "html.parser")
    links = soup.find_all('a')
    for n in links:
        rs = str(n.get_text())
        if re.match(pattern, rs):
            link_full =(url+rs)
            print (link_full)
            getReport(link_full)
            
except:
    print("Could not open", url)

