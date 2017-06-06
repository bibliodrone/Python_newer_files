#Extracting invoice numbers into a list in a text file
#from an invoice-derived text file (Aleph temp folder,
#or print invoice with option 'browse html', then copy-pase
#the "invoice lines" section.)


import re
import sys

def getInput():

  input = "atuagkat.txt"
  
  with open(input, "rt") as f:
    text = f.read()
    print (text)

    for line in text:
      re.match ('.[1-9]{8}.*', line)    
      
      
    print("Extraction Process Complete. ")

 
def main():
  getInput()
  

main()
