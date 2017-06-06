#ReadCal.py

import re
import csv

file = open ("ERINCAL.txt", encoding = "utf-8")
target = open("CALResult.csv", "w", encoding = "utf-8", newline="")

writer=csv.writer(target)

dtst = 'none'
desc = 'none'
summ = 'none'

writer.writerow(["Date","Collection","Note"])

for line in file:
    if line.startswith('END'):
        writer.writerow([dtst,summ,desc])
    else:
        if line.startswith('DTSTART'):
            dtst = (line[-9:]).rstrip()
        if line.startswith('DESCRIPTION'):
            desc = (line[12:]).rstrip()
        if line.startswith('SUMMARY'):
            summ = (line[8:]).rstrip()

file.close()
target.close()
