# EDI_report.py   v.20160722
# Gerald Walden 
# Returns data from the edi logs report page, filtered either according
# to the first 3 letters of a vendor code, or by a 5-digit log number.

import urllib.request
from bs4 import BeautifulSoup
import re
import sys
import datetime

def getReport(vendor):
# Can use chars between the date format tokens as separators (eg. %Y-%m-%d)
    date_string = f"{datetime.datetime.now():%Y%m%d}"
    print ("Getting Report ", vendor, '\n')
    url = ('http://lms01.harvard.edu/EDI_Invoices/edi_logs_report.html')

    data = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(data, "html.parser")

    tags = soup ('tr')
    file_r = "EDIlogHTML"+date_string+".txt"
    with open (file_r, 'w') as fr :
        for line in soup:
            fr.write(str(line))
        
    file_n = "EDI_Log_" + date_string +".txt"
    
    
    with open (file_n, "a") as EDIout:
        for tag in tags:
            Log = str(tag.contents[0].get_text())
            VDR = str(tag.contents[1].get_text())
            InvNo = str(tag.contents[2].get_text())
            line = (VDR + " " + InvNo + "   Aleph EDI Log " + Log + '\n')
            compare = re.compile(line[0:3])
    
            if compare.match(vendor):
                print("***", line, end = "")
                EDIout.write(line)

    print("\nReport Completed. File in PyNew folder is", file_n, "\n")
    getInput()

# 20170607 added text log output
def getLogNo(logNo):
    
    print ("Getting Report by Log Number -- ",logNo, '\n')
    url = ('http://lms01.harvard.edu/EDI_Invoices/edi_logs_report.html')
    
    data = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(data, "html.parser")

    tags = soup ('tr')

    for tag in tags:
        Log = str(tag.contents[0].get_text())
        VDR = str(tag.contents[1].get_text())
        InvNo = str(tag.contents[2].get_text())
        line = (Log + "  " + VDR + "  " + InvNo + "\n")
            
        compare = re.compile(Log)

        if compare.match(logNo):
            print(line, end = "")

    print("\nReport Completed.\n")
    getInput()

    

def getInput():
    vendor1 = input("Aleph Vendor Code or EDI Loads Log Number for which to search (type 'x' to quit) --> ")
    if vendor1 == 'x' or vendor1 == 'X':
            print("Shutting Down.")
            sys.exit(0)
            
    elif len(vendor1)>2 and vendor1.isalpha():
            vendor1 = '{: <5}'.format(vendor1)
            vendor2 = vendor1.upper()
            getReport(vendor2)
    elif len(vendor1)==5 and not(vendor1.isalpha()):
            getLogNo(vendor1)
    else:
            print("Please enter at least three letters.\n\n")
            getInput()

    
def main():
    getInput()

main()

