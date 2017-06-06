import csv
import re
#from pprint import pprint

replace=re.compile("[\[\]\']", "")

reportFile=open("resultsFile.csv")
Reader = csv.reader(reportFile)
reportData = list(Reader)

for item in reportData:
    for cell in item:
        print(replace.sub((str(cell))))

close(reportFile)

    
