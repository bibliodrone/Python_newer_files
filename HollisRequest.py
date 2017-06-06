import xml.etree.ElementTree as ET
import urllib.request
from bs4 import BeautifulSoup

#url = http://webservices.lib.harvard.edu/rest/marc/hollis/isbn/9782763728230
#url = http://webservices.lib.harvard.edu/rest/v2/classic/holdings/001252867
#url = http://webservices.lib.harvard.edu/rest/cite/hollis/011557057

url = "http://webservices.lib.harvard.edu/rest/classic/search/dc/psc=net%20safar"

data = urllib.request.urlopen(url).read()
soup = BeautifulSoup(data, "html.parser")

title = soup.find_all('title')
authorlast = soup.find_all('authorlast')
authorfirst = soup.find_all('authorfirst')

print(title[0].get_text(), end = " : ")
n = 0
for a in authorlast: 
        print(authorlast[n].get_text(), end = ", ")
        print(authorfirst[n].get_text(), end = "; ")
        n += 1
print("\n---------------------------------")
        
#for line in soup:
#        print (line)

#print(soup.prettify())
 
#root = ET.fromstring(data)
    
#callNo = root.iter('callnumber')

#allElem = root.iter()
#print (len(allElem))
#.find .findall .iter ... .get .text

#for item in callNo:
#        print (item.text)

'''		

#url = http://webservices.lib.harvard.edu/rest/v2/classic/holdings/001252867
Output:

*AC95.Up174R3.1971 (A) 
*AC95.Up174R3.1971 (B) 
AC95.Up174R3.1971 (C) 
PS3571.P4 R27 1971 
PS3571.P4 R27x 1971 
ALB 7214.321.20 

Page Source:

<?xml version="1.0" encoding="UTF-8"?>
<availability>
 <permalink>
  http://id.lib.harvard.edu/aleph/001252867/catalog
 </permalink>
 <branch>
  <repository>
   <id>
    HOU
   </id>
   <name>
    Houghton
   </name>
   <url>
    http://library.harvard.edu/ HOU
   </url>
  </repository>
  <collection>
   <collectionname>
    General Collection
   </collectionname>
   <holding>
    <callnumber>
     *AC95.Up174R3.1971 (A)
    </callnumber>
    <binding>
     Trade issue bound in publisher's red cloth over boards; top edges stained blue; with printed and illustrated dust jacket.
    </binding>
    <provenance>
     From the library of John Updike, with his ms. corrections.
    </provenance>
    <items>
     <itemrecord>
      <stat>
       Not checked out | In-library use
      </stat>
      <barcode>
       32044079932836
      </barcode>
      <lastreturndate>
       00000000
      </lastreturndate>
      <desc>
      </desc>
      <statuscode>
       02
      </statuscode>
      <processstatus>
      </processstatus>
     </itemrecord>
    </items>
   </holding>
  </collection>
  <collection>
   <collectionname>
    Harvard Depository
   </collectionname>
   <holding>
    <callnumber>
     *AC95.Up174R3.1971 (B)
    </callnumber>
    <binding>
     Limited issue bound in publisher's printed white, orange, and blue cloth, backed in blue cloth; top edges stained orange; in black, orange, and blue paper-covered slipcase.
    </binding>
    <provenance>
     From the library of John Updike.
    </provenance>
    <copyandversion>
     "Of the first edition of Rabbit Redux, three hundred and fifty copies have been printed on special paper and specially bound. Each copy is signed by the author and numbered."--Colophon; written in place of copy number: "Out of series"
    </copyandversion>
    <items>
     <itemrecord>
      <stat>
       Not checked out | Ask in Houghton Reading Room
      </stat>
      <barcode>
       HH3MQZ
      </barcode>
      <lastreturndate>
       00000000
      </lastreturndate>
      <desc>
      </desc>
      <statuscode>
       02
      </statuscode>
      <processstatus>
       Harvard Depository status
      </processstatus>
     </itemrecord>
    </items>
   </holding>
   <holding>
    <callnumber>
     AC95.Up174R3.1971 (C)
    </callnumber>
    <binding>
     Bound in publisher's red cloth over boards; top edges stained blue.
    </binding>
    <provenance>
     From the library of John Updike.
    </provenance>
    <copyandversion>
     This copy is from a collection of the author's works that the author kept together as a set, for purposes of recording changes and corrections for subsequent editions.
    </copyandversion>
    <copyandversion>
     With the author's manuscript corrections throughout, and a listing of the corrections on front flyleaf.
    </copyandversion>
    <copyandversion>
     Newspaper clipping of advertisement for Rabbit Redux affixed to front pastedown.
    </copyandversion>
    <items>
     <itemrecord>
      <stat>
       Not checked out | Ask in Houghton Reading Room
      </stat>
      <barcode>
       32044135104537
      </barcode>
      <lastreturndate>
       00000000
      </lastreturndate>
      <desc>
      </desc>
      <statuscode>
       02
      </statuscode>
      <processstatus>
       Harvard Depository status
      </processstatus>
     </itemrecord>
    </items>
   </holding>
  </collection>
 </branch>
 <branch>
  <repository>
   <id>
    KIR
   </id>
   <name>
    Kirkland House
   </name>
   <url>
    http://library.harvard.edu/ KIR
   </url>
  </repository>
  <collection>
   <collectionname>
    General Collection
   </collectionname>
   <holding>
    <callnumber>
     PS3571.P4 R27 1971
    </callnumber>
   </holding>
  </collection>
 </branch>
 <branch>
  <repository>
   <id>
    LAM
   </id>
   <name>
    Lamont
   </name>
   <url>
    http://library.harvard.edu/ LAM
   </url>
  </repository>
  <collection>
   <collectionname>
    General Collection
   </collectionname>
   <holding>
    <callnumber>
     PS3571.P4 R27x 1971
    </callnumber>
    <items>
     <itemrecord>
      <stat>
       Not checked out | 28-day loan
      </stat>
      <barcode>
       32044051838985
      </barcode>
      <lastreturndate>
       20160323
      </lastreturndate>
      <desc>
      </desc>
      <statuscode>
       28
      </statuscode>
      <processstatus>
      </processstatus>
     </itemrecord>
    </items>
   </holding>
  </collection>
 </branch>
 <branch>
  <repository>
   <id>
    WID
   </id>
   <name>
    Widener
   </name>
   <url>
    http://library.harvard.edu/ WID
   </url>
  </repository>
  <collection>
   <collectionname>
    General Collection
   </collectionname>
   <holding>
    <callnumber>
     ALB 7214.321.20
    </callnumber>
    <items>
     <itemrecord>
      <stat>
       Not checked out | Regular loan
      </stat>
      <barcode>
       32044021584776
      </barcode>
      <lastreturndate>
       20100727
      </lastreturndate>
      <desc>
      </desc>
      <statuscode>
       01
      </statuscode>
      <processstatus>
      </processstatus>
     </itemrecord>
    </items>
   </holding>
  </collection>
 </branch>
</availability>

'''
