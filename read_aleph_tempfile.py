
#input file with HTML to be searched
#input tag to search

#from bs4 import BeautifulSoup as BS
import re
#h_file = raw_input('File name: ')
#find_tag = raw_input('Find tag:')

h_file = "Aleph_invoice_html.txt"

with open(h_file, 'r', encoding='utf-8') as read:
    for line in read:
        line=line.strip()
        if re.search(".....order-number>[^<]", line):
            print(line[18:24])
        
        
       
        
