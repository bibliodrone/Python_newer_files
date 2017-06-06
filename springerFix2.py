import re

#some of these don’t actually appear in any fix file...
rep = {
'ADD-FIELD' : 'Add field: ',
'ADD-SUBFIELD' : 'Add subfield: ',
'FIXED-FIELD-EXTEND' : 'Extend fixed field length ',
'DELETE-FIELD' : '--> Delete this field unconditionally' ,
'SORT-FIELDS' : 'Sort all fields ',
'STOP-SCRIPT' : 'Stop Script from running ',
'CHANGE-FIELD' : 'Change field to ',
'DELETE-SUBFIELD' : '--> Delete subfield ',
'DELETE-SUBFIELD-DELIMITER' : 'Delete the subfield delimiter ',
'CHANGE-FIRST-IND' : 'Change first indicator of tag from',
'CHANGE-SECOND-IND' : 'Change second indicator of tag from',
'CHANGE-SUBFIELD' : 'Change subfield ',
'CONCATENATE-FIELDS' : '--> Copy field data to ',
'COPY-FIELD' : 'Copy contents of this field to a new ',
'DELETE-FIELD-COND' : 'Delete this field if (includes the following text?) = ',
'EDIT-SUBFIELD-HYPHEN' : 'something about hyphens, I guess.',
'FIXED-CHANGE-VAL' : ' Change value in fixed field position from ',
'FIXED-CHANGE-VAL-RANGE' : ' Change value in fixed field range ',
'REPLACE-STRING' : 'Replace ',
'CHANGE-FIRST-IND-MATCH' : 'Change first ind. if matches: ',
'CHANGE-SECOND-IND-MATCH' : 'Change second ind. if matches: ',
'COPY-SYSTEM-NUMBER' : 'Copy this system number to a new field: ',
'FIXED-RANGE-OP' : 'Nothing yet',
'COND-LOAD-VAL-POS' : 'Nothing yet',
'DELETE-FIXED-COND' : 'Nothing yet',
} 

section = 0

#g=open('fix_txt/generic.ebook.fixstripped.txt', 'w') #when writing to file, will have to change 'print' stmts back to 'write'
with open('fix_txt/generic.ebook.fixstripped.txt', 'rt') as f:
    print("\n\n")
   

    for line in f:
        if line[0].isnumeric() and line[0]!=section: 
            section = line[0]
            print("---Section " + str(section)+" ---\n")
    
        if line[0] == "!":
            print ("\t",line,end='')
    
        else:
            a = str(line[2:7]) #field tag
            if int(section) > 1 and re.search("LDR", a):
                a = "   " #In the main fix script body (section 2 and on), LDR doesn't really mean anything.

            b = str(line[13:16].strip()) #fixed field range start
            b1 = str(line[17:20].strip()) #fixed field range end (if range > 1)

            occ = str(line[21:26].strip()) #"Occurrence" conditional; values include NOT-F or NOT-L (not first, or not last)

            c = str(line[27:57].strip()) #Operation Code      

            d = str(line[58:100].rstrip()) #Operation Parameters
            #d = d.replace("#", "(any value)") #Reformatting Parameters to read more like a sentence
            d = d.replace(",L,", "")
            d = d.replace("Y,", "Yes--> ")
            if d.endswith(","):
                d = (" " + d[:len(d)-1] + ", \s ")
            d=d.split(",")
        
        #g.write
            print("//", a, end="")
            print(" ", b, end="")
            if len(b1)>2 and not(b == b1): print(" to: ", b1) #Formatting any fixed field parameter codes
            if c in rep: print(rep[c], end="") #Looking up Op. code in dictionary, to replace with friendlier text
            if len(occ)> 2: #If there's anything in the Occurrence filter...
                #print(occ)
                if re.search("NOT-L", occ):
                    print(" if not the last occurrence of this field ", end='')
                elif re.search("NOT-F", occ):
                    print(" if not the first occurrence of this field ", end='')
            #print(str(d) + "\n")
            #print(str(d[:len(d)]), "\n")
            if re.search("REPLACE", c):  #Attempting to add some reader-friendly and syntactically correct prepositions.
                d=" with: ".join(d)
            elif re.search("CHANGE",c):
                d=" to: ".join(d)
            else:
                d="".join(d)
            print(str(d),"\n")
       
print("The symbol '\s' signifies 'space' or 'blank'") #Just in case this is a new thing

f.close()
#g.close()
