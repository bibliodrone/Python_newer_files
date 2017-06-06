#Extracting invoice numbers into a list in a text file
#from an invoice text file in Aleph Temp folder

import re


inFile = input("Enter Filename: ")

f=open(inFile)
g=open("BlistFile.txt", 'w')

for line in f:
    if re.match ('^.[0-9]{8}.*', line):
	    g.write(line)

f.close()
g.close()


