import re, pprint

# identify the unique tags present in hollis search result XML

brackets = re.compile("(^)(<[^\s][^>]+>)(.*$)")

tags = []
records = []

with open ('amatthew.txt', 'r', encoding = 'utf-8') as am:
    for line in am:
        if "cataloglink" in line:
            records.append(line[45:54])
"""            
            
        if "<" in line:
            if "/" in line:
                line = line.replace("/", "")
            line = re.search(brackets, line)
            line = line.group(2)
            if "item" in line:
                line = "<item>"
            
            tags.append(line)
        else:
            continue
tags = set(tags)
pprint.pprint(tags)
"""
