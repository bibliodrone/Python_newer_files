import re

OpsDict = {
'ADD-FIELD' : 'Adds Field OP1, OP2, OP3',
'FIXED-FIELD-EXTEND' : 'Extends length of fixed field if at least OP1 to OP2 with padding OP3',
'REPLACE-STRING-GENERAL' : 'Replaces OP1 with OP2',
'DELETE-FIELD' : 'Deletes Field',
'SORT-FIELDS' : 'Sorts Fields',
'STOP-SCRIPT' : 'Stops Script from running',
'CHANGE-FIELD' : 'Changes Field tag to OP1',
'DELETE-SUBFIELD' : 'Deletes tag subfield (occurence NOT-L only if not last)',
'DELETE-SUBFIELD-DELIMITER' : 'Nothing yet',
'CHANGE-FIRST-IND' : 'Changes first indicator of tag from OP1 to OP2',
'CHANGE-SECOND-IND' : 'Changes first indicator of tag from OP1 to OP2',
'CHANGE-SUBFIELD' : 'Changes tag subfield OP1 to OP2',
'CONCATENATE-FIELDS' : 'Nothing yet',
'COPY-FIELD' : 'Copies contents of field tag to OP1',
'DELETE-FIELD-COND' : 'Deletes field tag if OP2 is present',
'EDIT-SUBFIELD-HYPHEN' : 'Nothing yet',
'FIXED-CHANGE-VAL' : 'Changes tag range start from OP1 to OP2',
'FIXED-CHANGE-VAL-RANGE' : 'Nothing yet',
'REPLACE-STRING' : 'In tag replace OP1 with OP2',
'CHANGE-FIRST-IND-MATCH' : 'Nothing yet',
'CHANGE-SECOND-IND-MATCH' : 'Nothing yet',
'COPY-SYSTEM-NUMBER' : 'Copies the contents of tag to create OP1 OP2 OP3 OP4',
'FIXED-RANGE-OP' : 'Nothing yet',
'COND-LOAD-VAL-POS' : 'Nothing yet',
'DELETE-FIXED-COND' : 'Nothing yet',
}
g=open('sliced.txt', 'w')
with open('cleansprgr.txt', 'rt') as f:

    for line in f:
        a = str(line[2:5].rstrip())
        b = str(line[13:16].rstrip())
        c = str(line[27:57].rstrip())       
        d = str(line[58:100].rstrip())
        d = d.replace("#", "*any* ")
        if d.endswith(","):
            d = (d + "with blank")
                  
        g.write("Field " + a)
        g.write(" " + b)
        g.write(" " + c.title())
        g.write(" " + d + "\n")

g.close()
        
##        L[0].append(a)
##        L[1].append(b)
##        L[2].append(c)
##        L[3].append(d)

#print(line[2:5] +" "+ line[13:16]+" " + " " + line[27:50]+ " " + line[58:100])
##for i in L:
##    print(L[0][i] + " " + L[1][i] + " " + L[2][i] + " " + L[3][i] + " " + L[4][i], end = '')

##def parseText(text)
