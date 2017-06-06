import urllib.request
from bs4 import BeautifulSoup
import re
import sys

def testPull():

    url = ("http://lms01.harvard.edu/mars-reports/jun-16-data")
    data = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(data, "html.parser")
    tags = soup('a')

    skan = re.compile("^R13.+")

    for tag in tags:
        if skan.match(tag.get_text()):
            return(tag.get_text())
            break
        else:
            continue

def listReports():

    url = ('http://lms01.harvard.edu/mars-reports/')

    data = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(data, "html.parser")

    tags = soup('a')

    compare = re.compile("^[\w]{3}-[\d]{2}-data")

# note: break, continue, pass (not followed by () )
# pass skips over a step, but continues the loop.

    for tag in tags:
        if compare.match(tag.get_text()):
            return(tag.get_text())
            break
        else:
            continue

# next, def getReports()
# incorporates Target_Date ; http://lms01.harvard.edu/mars-reports/jun-16-data/
# searches through list to find desired R13 files and
# pull them in for futher fun times.
    
def main():
    Target_Date=str(listReports())
    print("Target Date: ", Target_Date)
    Target_Report=str(testPull())
    print("Target Report: ", Target_Report)
    
main()




