import re

#read textfile from bs4 dump

iid = re.compile('(^.*id=")([^"]*)(\".*$)') # Item id
catlink = re.compile('(.cataloglink.)([^<]*)(<.+$)') # catalog http link
ttl = re.compile('(.title.)([^<]*)(<.+$)') # title(s)
typ = re.compile('(.dc.type.)([^<]*)(<.+$)') # type of item (database...?)
adam = re.compile('(<dc:)([^>]*)([^>]*)(<.+$)')
                     

with open("amatthew.txt", "r", encoding = "utf-8") as am:


    for line in am:
        if "item id" in line:
            line = str(re.search(iid, line).group(2))
            print()
            print(line)
        elif "cataloglink" in line:
            line = str(re.search(catlink, line).group(2))
            print(line)
        elif ":title" in line:
            line = str(re.search(ttl, line).group(2))
            print(line)
        elif ":type" in line:
            line = str(re.search(typ, line).group(2))
            print(line)
        elif "Adam Matthew" in line:
           line = str(re.search(adam, line).group(2).group(3))
