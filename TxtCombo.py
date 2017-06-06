# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 17:56:19 2017

@author: walden
"""
import os
#import glob



#filePath="C:\\Users\\walden\\Desktop\\37880txt"

#print(os.getcwd())

try:
    os.chdir("C:\\Users\\walden\\Desktop\\37880txt")
    print(os.getcwd())
    #read_files = glob.glob("ch*\*.txt")
    """
    with open("37880result.txt", "wb") as outfile:
        for subdir, dirs, files in os.walk():
            for f in files:
                with open(f, "rb") as infile:
                    outfile.write(infile.read())
                    outfile.write("__________________\n\n")"""
except:
    print("File not found in PyNew")           