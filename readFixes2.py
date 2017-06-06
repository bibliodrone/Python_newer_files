#readFixes2.py

import re

ff = "safari.fix.txt"

file = open(ff, encoding = "utf-8")

print ("Reading file ", ff)
for line in file:
    if line [1:4] == "rem":
        print (line [5:])
    if re.match("^![\s\d]", line):
        continue
    elif line[0] == '1' or line[0]== '2':

        c2=line[2:7].strip() #tag -- 5 chars
        c5=line[12:16].strip() #position range st -- 3 chars
        c6=line[17:20].strip() #position range end -- 3 chars
        c7=line[21:26].title() #occurrence filter -- 5 chars
        c8=line[27:56].title() #operation code -- 30 chars
        c9=line[58:] #operation parameters -- up to 100 chars

        if not c9.startswith("Y"):
            c9=c9.split(",")

        newLine = (c2, c5, c6, c7, c8, c9)
        for e in newLine: print (e, end = "")
        print()
        if newLine[0] == 'ADD-FIELD':
            print("Add Field :", newLine[6][1], " to ", newLine[6][2])
"""
        if c2.startswith("T"): print()
        if c8.startswith ("ADD-FIELD"):
            print ("Add field ", c9[0:4], " " ,c9[5:].rstrip())
        if c8 == "ADD-SUBFIELD": 
            print ("Add subfield ", c9.rstrip(), " to ", c2)
        if c8 == "CHANGE-FIELD":
            print("Change field ", c2 , " to " , c9.rstrip())
        if c8 == "CHANGE-FIRST-IND" or "CHANGE-SECOND-IND" or "CHANGE-FIRST-IND-MATCH" or "CHANGE-SECOND-IND-MATCH"or "CHANGE-SUBFIELD":
            print ("Field ", c2, " " , c8.title(), " " , c9.rstrip()) 
        if c8 == "CONCATENATE-FIELDS":
            print ("change ", c2, " to ", c9.rstrip())
        if c8 == "COPY-FIELD":
            print ("copy ", c2, " to ", c9.rstrip())
        if c8 == "COPY-SYSTEM-NUMBER":
            print ("Copy Sys. no from ", c2," to create ", c9.rstrip(), c2)  
        if c8 == "DELETE-FIELD":
            print ("Delete ", c2)
        if c8 == "DELETE-FIELD-COND":
            print ("Delete ", c2," if --> is present :", c9[1:].rstrip(), " equals ", c9[0])
        if c8 == "DELETE-SUBFIELD":
            print("Delete subfield ", c9.rstrip(), " from ", c2) 
        if c8.startswith ("FIXED-CHANGE-VAL"):
            print ("change ", c2, " position ", c5," to ", c9[1:].rstrip(), " if matches ",c9[0])
        if c8 == "FIXED-CHANGE-VAL-RANGE":
            print ("change ", c2, " position ", c5," to ",c6," to ", c9[1:].rstrip(), " if matches ",c9[0])
        if c8 == "FIXED-FIELD-EXTEND":
            print ("Extend field ", c2, " to minimum length of 14.")
        if c8 == "REPLACE-STRING":
            print ("In ", c2, " Replace: ", c9.rstrip())
"""

file.close()
        
                   
        
