from bs4 import BeautifulSoup
#import urllib.request
#url =('http://webservices.lib.harvard.edu/rest/mods/hollis/isbn/9783902968210')

f = ('Aleph_invoice_html.txt')
z_tag = ('z68-order-number')

#isbn = '9783902968210'
#data=urllib.request.urlopen(url).read()

data = open(f)

soup = BeautifulSoup(data, 'lxml')

tags=soup.find_all(z_tag)

first_tag = tags[0].contents[0]

fname = str(first_tag) + ".txt"

with open(fname, 'w') as f:
    for t in tags:
        if t.contents:  #...ignores blank tags
          print(t.contents[0]) #print just the text
          f.write(str(t.contents[0])+"\n")

print ("List-file name:", fname)
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


