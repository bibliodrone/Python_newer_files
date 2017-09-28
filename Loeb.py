import re

notabs = re.compile('([^\t]+)')
with open('HUP_Global_LoebClassics_2017-06-26.txt', 'r') as loeb:

    lclassics = []

    for line in loeb:
        subline = (notabs.findall(line))
        catalog = ""
        
        for item in subline:
            if item.startswith("http"):
                print(item, end=" -- ")
        print(subline[0])
	
