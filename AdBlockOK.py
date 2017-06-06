#Extracting comment lines from AdBlock's acceptable Ads list

import re

with open("adblock.txt", encoding = 'utf-8', mode='r') as f: # good to specify encoding; sometimes default is ANSI
    g=open("AdExcepts2.txt", encoding = 'utf-8', mode='w')   # and in this case there were Cyrillic letters present, too. 

    lineCounter=0
    
    for line in f:
        try:
            if re.match("^(\! \w).+$", line):
                g.write(line)
                lineCounter+=1
                
        except Exception as e:
            print ("Error in line ", lineCounter, " ",e.args)
            lineCounter=+1
            continue
f.close()
g.close()


