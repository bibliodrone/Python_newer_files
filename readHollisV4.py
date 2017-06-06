#reading output file from HollisRequestV4.py
import re

pattern=re.compile("(^<)(item id\=)(\")([0-9]+)(\")(.*>)$")
total_results=re.compile("(<)(totalResults)(>)([0-9])(<//.*>)$")

with open ('outHvd.txt', 'r') as reader:
    for line in reader:
        if re.search(total_results, line):
            st1=str(re.search(total_results, line).group(4))
            print("Total Results", st1)
        if re.search(pattern, line):
            st = str(re.search(pattern, line).group(4))
            print (st)
