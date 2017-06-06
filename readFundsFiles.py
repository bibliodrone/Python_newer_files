# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 17:56:19 2017

@author: walden
"""
import os

os.chdir('C:\\Users\\walden\\Desktop\\textfolder')#put the whole path in there...
files = os.listdir('.')

for i in range(len(files)):
    print("\n\n")
    with open(files[i], 'r') as f:
        fstr = str(files[i])
        print("\n------",fstr[:-4],"------\n")
        for line in f:
            print(line.replace("&",""), end="")
'''
Above assumes only text files in the target folder. 

From StackOverflow--example that targets by file extension.

EXTENSIONS = ('.cpp','.hpp')

for root, dirs, files in os.walk(top):
    for file in files:
        if file.endswith(EXTENSIONS):
            #file which ends with extension type so do your thing!
'''

