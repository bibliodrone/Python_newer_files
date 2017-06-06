#readCons.py

import re

addy=re.compile("\w.+@\w.+.\w+.\w\w\w")

writeTo = open ("writeTo.txt", "w", encoding = "utf-8")

with open("udetailsOAB.txt", "r") as OL:
    for line in OL:
        line=line.strip()
        try:
            lineout = re.search(addy)
            if addy:
                writeTo.write(addy)
        except:
            continue
writeTo.close()

        
