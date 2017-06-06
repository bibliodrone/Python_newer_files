# Built to gather all of the 37880 fund info from the Budget Macro files,
# to use in planning for the WLD changeover to 37861
import os
import glob

pfad = os.getcwd() + '\\FundMenus'
os.chdir(pfad)

file_list = glob.glob("*.txt")

with open('budgetsFull.txt', 'w') as outfile: 
    for fname in file_list:
        print(fname, end = "; ")
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
print("Process Complete")

"""

 
    print("Complete!"
    print(root, "consumes", end=" ")
    print(sum(getsize(join(root, name)) for name in files), end=" ")
    print("bytes in", len(files), "non-directory files")
    if 'CVS' in dirs:
        dirs.remove('CVS')  # don't visit CVS directories
"""
