# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

from BeautifulSoup import BeautifulSoup
import urllib2
url="http://www.sudoc.fr/171178092.rdf"
page=urllib2.urlopen(url)
soup = BeautifulSoup(page.read())
isbns=soup.findAll('bibo:ISBN13')
for eachisbn in isbns:
   print eachisbn['href']+","+eachisbn.string

# <codecell>


# <codecell>


