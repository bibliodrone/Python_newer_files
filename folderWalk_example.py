# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 18:29:51 2017

@author: walden
"""
#import glob
import os
import re

pattern = re.compile("\.py$")

rootdir = 'C:/Users/Walden/Desktop/PyNew/Python3_Standard_Library'
print("Root Directory: ", rootdir)
print("Displaying names of Python files in all directories and sub-directories")
print("-----------------------------------")
#with open("resultaten.txt", "wb") as outfile:
for subdir, dirs, files in os.walk(rootdir):
    for f in files:
        if re.search(pattern, f): print("***", subdir, f)
        else: print(subdir, f)
            
"""
                with open(f, "rb") as infile:
                    outfile.write(infile.read())
                    outfile.write("__________________\n\n")
            
        print (os.path.join(subdir, file))
        read_files = glob.glob("*.py")


        
