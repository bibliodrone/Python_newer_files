# Made this to take a census of the H drive to see if there really is some
# reason why it looks almost full. This result, though, simply mirrors
# what Windows was saying. 40GB vs. 700GB+? Who knows...?

import re

patt = re.compile("^..\/..\/20..[^<]+$")

with open ('filedir.txt', 'r') as f:
    sumtotal = 0
    out = " "
    uhrray = []
    for line in f:
        out = line.strip()
        if (re.search(patt,out)):
            ln = len(out)
            bytes = out[21:39].strip()
            flnm = out[39:ln].strip()
            dig = int(bytes.replace(",",""))
            dt = out[0:10]
            sumtotal = sumtotal + dig
            #if len(str(dig))> 5:
                #print(out)
            uhrray.append(dt + ", " + str(dig)+ ", " + flnm + "\n")
            
    print(sumtotal)
    print(len(uhrray))

    with open('Hsuspects.txt', 'w') as hd:
        for item in uhrray:
            hd.write(item)
    
    '''
    if fs.endswith('bytes'):
        fs=(fs.split('(s)')[1].strip()[:-6])
        fs=fs.replace(',','')
        fs = int(fs)
        bits = bits + fs

    print("Bits: ", str(bits))
    '''

           


