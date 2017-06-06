import urllib.request
from bs4 import BeautifulSoup

url = ('http://lms01.harvard.edu/EDI_Invoices/edi_logs_report.html')

data = urllib.request.urlopen(url).read()
soup = BeautifulSoup(data)

tags = soup ('th')

for tag in tags:
	print (tag.contents[0])


#XPath from the Google Sheets:	/html/body/center/p/table/tbody/tr[1]/th[1]