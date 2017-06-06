#Reformats ebook fix (text) to remove commented sections, leaving only the active code portions for study and parsing.
#Files acted upon were in the fix_txt folder, but now only the reformatted files are there; the originals are in a sub-folder.

import os
import re

path = 'fix_txt/'
listing = os.listdir(path)

for infile in listing:
    cleanName = (str(infile)[:-4]) #remove file suffixes
    fullPath = path + infile #specify that new files go in fix_txt folder
    print (cleanName)
    f = open (fullPath, 'r') #original file
    g = open (path + cleanName + "stripped.txt", 'w') #"comments-removed" file, renamed to .txt w/o .fix
    for line in f:
        if line[0] != '!':
            g.write(line)
        if re.search("^!rem.+", line): #Only write lines not starting with a 'bang' to the new .txt file.
            g.write(line)               
    f.close()
    g.close()

print('operation complete')
