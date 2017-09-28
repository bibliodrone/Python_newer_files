ibnlist = []
with open ('safariNotAvail.txt', 'r') as s:
    for line in s:
        ibnlist.append(line[1:len(line)-2])

        
