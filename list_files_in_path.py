# -*- coding: utf-8 -*-
"""
Created on Wed Sep 6 2017
Adapted from folderWalk_example.py

@author: walden
"""

import os
import re
import time

def main():
    get_user_input()
    
def get_user_input():
    rootdir = input("Root directory: Enter a complete directory path...")
    filetype = input("File type filter, e.g.: .txt (just hit enter for none)")
    if filetype == "":
        list_dir_re("none", rootdir) # If no filetype, just go straight to listing
    elif len(filetype) == 4:
        filetype = filetype[1:] #crude way of removing a '.'

    validate_file(filetype, rootdir) # If filetype specified, validate the string entered

def validate_file(filetype, rootdir):    
    if len(filetype) == 3:
        if filetype.isalpha():
            pattern = re.compile(filetype + "$")
            list_dir_re(pattern, rootdir)
        else:
            print(str(filetype), "is not valid.")
            print(">>> File types are usually three letters, eg. txt for text files")
           
            get_user_input()
"""
def list_dir(rootdir):    
#try:
    ln = len(rootdir)
    print()
    print("-----------------------------------")
    
    for subdir, dirs, files in os.walk(rootdir):
        print("\n~\\" + subdir[(ln+1):])
        for f in files:
            fullpath = rootdir + '\\' + f
            ftime = file_mod_time(fullpath)            
            #ftime = "ERROR"
            print("   ", f, end = "     ")
            print(ftime)


except:
    print("That does not appear to be a valid directory path.")
    try_again = input("Try again?")
    if try_again in ('Y', 'y'):
        get_user_input()
    else:
        print("Goodbye.")
        exit
"""
def list_dir_re(pattern, rootdir):
#try:
    ln = len(rootdir)
    print()
    print("-----------------------------------")
    
    for subdir, dirs, files in os.walk(rootdir):
        for f in files:
            fullpath = subdir + "\\" + f
            ftime = file_mod_time(fullpath)
            if pattern == "none":
                print("\n~\\" + subdir[(ln+1):], end = "  >>>  ")
                print(f, end = "     ")
                print(ftime, end = "")  
            
            elif re.search(pattern, f):
                print("   ", f, end = "     ")
                print(">>>", ftime)
            
    print("\n\n *** Listing complete.")
    
"""
except:
    print("That does not appear to be a valid directory path.")
    try_again = input("Try again?")
    if try_again in ('Y', 'y'):
        get_user_input()
    else:
        print("Goodbye.")
        exit
"""
def file_mod_time(f):
    
    ftime = os.path.getmtime(f)
    ftime = time.ctime(ftime)
    return ftime
"""
mtm = os.path.getmtime("full\file\path") returns float, e.g. 1430765715.9864137
time.ctime(mtm) returns 'Mon May  4 14:55:15 2015'
"""

if __name__ == "__main__":
    main()
