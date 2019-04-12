# crdp.py
#
# Gerald Walden, Harvard Library ITS
# 11/20/2017
#
# Downloads into current working directory marc files posted on
#  - lamont url = "http://web.marcive.com/httpdownload/?l=ftp&s=wglzfnky"
#  - law url = "http://web.marcive.com/httpdownload/?l=ftp&s=5Q555Pcb"
# 
# > Targets file anchor-tags;
# > Follows them to start the file download;
# > Saves the files to the working directory; 
# > By default, downloaded files lack any extension,
#   so '.mrc' extension is added as a final step.
#
# > Other scripts can be used with the results of crdp.py to
#   rename the downloaded files, and to automatically run the
#   MarcBreaker feature via cmarcedit.exe
# ===============================================================
# MARCIVE File naming conventions:
# - Filename will reflect month previous to download (e.g. April 2019
#   downloads are named with "March2019"
#
# - Filenames starting with 'G084': Lamont
# - Filenames starting with 'G130': Law
# - Files of new monograph and serial additions: (NEWONLI/NEWSER)
# - Files of changed/removed records: (CHGONLI/CHGSER)
# 
# CRDP Marcive E-monographs monthly load documented at:
#  'https://wiki.harvard.edu/confluence/x/nwlzBQ'

#

from bs4 import BeautifulSoup as bs
import urllib.request as req

def read_page(url):

    with req.urlopen(url) as r:
        soup_page = r.read()
        soup = bs(soup_page, "lxml")
        links = soup.find_all('a')
        avail = soup.find_all('div',{'class':'available'})[0].get_text()
        print(avail)
        return(links)
    
def ftp_me(lib, url):
    for item in lib:
        file_target = (url + "&file=" + item.string)
        print("\nRetrieving", file_target)
        try:
            req.urlretrieve(file_target, item.string + ".mrc")
        except: 
            print("\nWas not able to retrieve", file_target)

def main():
    lamont = ""
    law = ""
    lamont_url = "http://web.marcive.com/httpdownload/?l=ftp&s=wglzfnky"
    law_url = "http://web.marcive.com/httpdownload/?l=ftp&s=5Q555Pcb"
    
    try:
        print("\n >>> Trying to read from ", lamont_url)
        print()
        lamont = read_page(lamont_url)
    except:
        print("\nThere was a problem reading from the Lamont url\n")

    try:
        print("\n >>> Trying to read from ", law_url)
        print()
        law = read_page(law_url)
        
    except:
        print("\nThere was a problem reading from the Law url\n")
    
    ftp_me(lamont, lamont_url)
    ftp_me(law, law_url)
    print()

#if __name__ == "__main__":

main()

