# Read Adam Matthew files created with 'adamMatthewQuery.py'

import bs4

#fnames = ["AmatthewQuery0.txt", "AmatthewQuery1.txt", "AmatthewQuery2.txt", "AmatthewQuery3.txt"]

fname = "AmatthewQuery0.xml"

dataArray = []

#for f in fnames:
with open (fname, "r", encoding = "utf-8") as am:
    soup = bs4.BeautifulSoup(am, "lxml")
    id = soup('#id')
    print(id.getText())

         
        
        
        
