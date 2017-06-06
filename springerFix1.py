#Fix translator (Springer prototype)

import re

"""
def replace(c):
    c=c.replace('ADD-FIELD', 'Add Field ')
    c=c.replace('FIXED-FIELD-EXTEND', 'Extend fixed field length')
    c=c.replace('DELETE-FIELD', '<-- Delete Field')
    c=c.replace('DELETE-FIELD-COND', 'Delete field if contains,')

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
"""
g=open('sliced.txt', 'w')
with open('cleansprgr.txt', 'rt') as f:

    for line in f:
        a = str(line[2:5].rstrip())
        b = str(line[13:16].rstrip())
        b1 = str (line[17:20].rstrip() + " ")
        c = str(line[27:57].rstrip())
        d = str(line[58:100].rstrip())
        d = d.replace("#", "*any*")
        d = d.replace(",L,", "::")
        if d.endswith(","):
            d = ("'" + d[:len(d)-1] + "' --> \s")
        d=d.split(",")
                  
        g.write("// " + a)
        g.write("  " + b)
        if len(b1)>2: g.write(" to " + b1)
        g.write(str(c).title() +" ")
        #g.write(str(d) + "\n")
        #print(str(d[:len(d)]), "\n")
        d=" --> ".join(d)
        g.write(str(d) + "\n")
       
g.close()
        
##        L[0].append(a)
##        L[1].append(b)
##        L[2].append(c)
##        L[3].append(d)

#print(line[2:5] +" "+ line[13:16]+" " + " " + line[27:50]+ " " + line[58:100])
##for i in L:
##    print(L[0][i] + " " + L[1][i] + " " + L[2][i] + " " + L[3][i] + " " + L[4][i], end = '')

##def parseText(text)
