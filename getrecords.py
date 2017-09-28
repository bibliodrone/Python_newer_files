#GetRecords.py
#Hollis ISBN search; returns list of holding libraries, and the Record ID.

import re
import urllib.request
from bs4 import BeautifulSoup

url=('http://webservices.lib.harvard.edu/rest/mods/hollis/isbn/9780307269751')

data = urllib.request.urlopen(url).read()

rem = re.compile("<\w+>.+")

soup = BeautifulSoup(data, "html.parser")
physLoc = soup.find_all('physicallocation')
recID = soup.find_all('recordidentifier')
Those = soup.find_all('*')

r = re.search(rem, soup)


print("Sys no.: " + recID[0].get_text())


        








