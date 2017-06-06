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
##for k, v in OpsDict.items(): print(k + ": " + v)

#g=open('sliced.txt', 'w')

operation=" "

with open('cleansprgr.txt', 'rt') as f:
    for line in f:
        
#        for k, v in OpsDict.items():
        if (line[0]==' '):
            print("Comment: " + line)
###            g.write("comment: " + line)
        else:
            entry = line[27:57].rstrip()
            print (OpsDict.get(entry))
##            operation =(line[27:57])
##            print(OpsDict.get(operation))
####            for key, val in OpsDict.items():
####                if key == operation:
####                    print(key)
###                    g.write(val + "\n")
##
###g.close()
