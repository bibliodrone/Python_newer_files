import re

ff = "safari.fix.txt"

file = open(ff, encoding = "utf-8")

print ("Reading file ", ff)
for line in file:
    if line [1:4] == "rem":
        print (line [1:])
    if re.match("^![\s\d]", line):
        continue
    elif line[0] == '1' or line[0]== '2':
        c2=line[2:7] #tag -- 5 chars
        c5=line[12:16] #position range st -- 3 chars
        c6=line[17:20] #position range end -- 3 chars
        c7=line[21:26].title() #occurrence filter -- 5 chars
        c8=line[27:56].title() #operation code -- 30 chars
        c9=line[58:] #operation parameters -- up to 100 chars

       # if len(c9.strip())>1:
        c9.split(',',2)
             
        s = ""
   
        #print(c2.rstrip(), c5.rstrip(), c6.rstrip(), c7.rstrip(), c8.rstrip(), c9.rstrip())  
        #print(len(line))
        if c2=="LDR" or c2=="008":
            print(c2, " ", end='')
        else:
            print("Field ",c2, end=": ")
        if len(c5.strip())>1:
            print("position", c5, "; ", end = '')

        if c7 == "NOT-F":
            s=("If not the first occurrence of")
        elif c7 == "NOT-L":
            s=("If not the last occurence of")
        elif c7 == "FIRST":
            s=("If this is the first occurence of")
        elif c7 == "LAST":
            s=("If this the final occurence of")
         
        if len(s)>1:
            print(s,c2,"then", c8)
            continue
        
        if re.match("\S", c8):
            if c8.startswith("Replace"):
                print ("Replace--> ", c9[0], "with--> ", c9[1], end = '')
            else:    
                print(c8," ", end = '')
                if len(c9)> 0:
                    print (c9, end='')
        else:
            print()

     #   if re.match(".*DELETE-FIELD-COND.", line):
    #    print ("Delete field ", line [2:5], "if it contains the text: ", line[60:])

file.close()

'''
define (fields):
    field = line[2:8]
    fRange = line[13:20]
    Cond = line[21:26]
    Operation = line [27:45]
    parameters = line[57:80]
 Note : index 1 and 2: control fields, other bib fields, Index 7,8 for formatting 035
 
'''
def matchOp(op):
    if op == "ADD-FIELD":
        return 
    elif op == "ADD-SUBFIELD":
        asf(op)
    elif op == "CHANGE-FIELD":
        cf(op)
    elif op == "CHANGE-FIRST-IND" or "CHANGE-SECOND-IND" or "CHANGE-SUBFIELD":
        cfi(op)
    elif op == "CHANGE-FIRST-IND-MATCH" or "CHANGE-SECOND-IND-MATCH":
        cfim(op)
    elif op == :
        csi(op)
    elif op == 
        (op)
    elif op == ""
        (op)
    elif op == ""
        (op)
    elif op == ""
        (op)
    elif op == ""
        (op)
    elif op == ""
        (op)
    elif op == ""
        (op)
    elif op == ""
        (op)
    elif op == ""
        (op)
    elif op == ""
        (op)
    elif op == ""
        (op)
    elif op == ""
        (op)
    elif op == ""
        (op)
    elif op == ""
        (op)
    elif op == ""
        (op)
    elif op == ""
        (op)
    elif op == ""
        (op)
     

        
