# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 18:29:51 2017

@author: walden
"""
'''import glob'''
import os
import re

pattern = re.compile("*.py")

rootdir = 'C:/Users/Walden/Desktop/PyNew/Python3_Standard_Library'

with open("resultaten.txt", "wb") as outfile:
    for subdir, dirs, files in os.walk(rootdir):
        for f in files:
            if re.match(f, pattern):
                print(f)
            else: print("none")
            
"""
                with open(f, "rb") as infile:
                    outfile.write(infile.read())
                    outfile.write("__________________\n\n")
            
        print (os.path.join(subdir, file))
        read_files = glob.glob("*.py")
"""
        