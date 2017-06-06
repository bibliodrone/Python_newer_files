import os

pfad = os.getcwd() + "\\FundMenus"
os.chdir(pfad)
#could use root, dir as well as files.

for root, dirs, files in os.walk("."):
    for name in files: 
        with open(name, "r") as reading:
            for line in reading:
                print(name[:12] +  ".." + line, end = "")
"""         
    print("Complete!"
    print(root, "consumes", end=" ")
    print(sum(getsize(join(root, name)) for name in files), end=" ")
    print("bytes in", len(files), "non-directory files")
    if 'CVS' in dirs:
        dirs.remove('CVS')  # don't visit CVS directories
"""
