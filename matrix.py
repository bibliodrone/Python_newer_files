#matrix.py -- using csv, a bit of formatting, control logic

import csv
import re

again = "x"

def vendorSearch():
    ordUnits = ("WIDEU", "WIDCN", "FAL01")#Order units filter

    vLetter=""

    while len(vLetter)<1:   #Check input for len>0, alphanumeric
        while not(str.isalpha(vLetter)):
            inp=input("Enter vendor: ")
            if len(inp)> 11: #Really long input, discard anything beyond 10 characters
                inp = inp[0:11]
            vLetter = str.lower(inp)
            print ()

    with open ('AdaptedFromDLMatrix.csv') as csvfile:   #Hardcoded csv file...
        reader = csv.DictReader(csvfile)
        e = len(vLetter)
        for row in reader:
            r = str.lower(row['Vendor'][0:e]) #refer to columns by header name; used 'str.' here also
            if r == vLetter:
                if row['Order_Unit'] in ordUnits: #Filters out all but ordunits specified in ordUnits
                    print('{:20} {:8} {:12}'.format (row['Vendor'], row['Order_Unit'], row['Account_No']))
                    #Format specifiers for columns of fixed width, to make output neater
    print()

while again[0] != str.lower("n"):
    vendorSearch()   
    again = input("Again? ")

