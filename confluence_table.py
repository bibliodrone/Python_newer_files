# confluence_table.py
# pick apart the HTML surrounding a table from Confluence

#from bs4 import BeautifulSoup as bs
import re

pattern = re.compile("<table.*>.+<\\table>")
with open("ConfluenceTableHTML.html", encoding ="cp1252") as h:
    for line in h:
        st = str(re.search(pattern, line))
        print (st)
        
#soup = bs(open("ConfluenceTableHTML.html"))
