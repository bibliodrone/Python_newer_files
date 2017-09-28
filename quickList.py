#quickList.py
import re
import os
import time

def main():
    now = time.time()
    stamp = str(now).replace(".", "")
    userName=os.getlogin()

    fn = "List_"+userName+".txt"
                            
    lf = open(fn, 'w')

    start = 0
    lng = 0
    xpattern = re.compile("[Xx]")
    ypattern = re.compile("\d+")

    print("Welcome back,", str(userName), ".\n")
    print()
    print("Quickly create a sequential list of order numbers for use with the \nAleph List Macro (Win + Alt + n) ")
    print("EDI orders beginning with X are fine, too.")
    print()
    print()  
    start = input('Enter first number in range: ')
    Nlines = input ('Enter number of items (excluding postage line): ')

    if xpattern.search(start):
        print()
        line()
        start = int(start[1:])
        Nlines = int(Nlines)
        for n in range(0, Nlines):
            print("X" + str(start+n))
            lf.write("X" + str(start+n)+"\n")
        print()
        print("File '"+fn+"' created.")
        lf.close()
        
    elif ypattern.search(start):
        print()
        line()
        start = int(start)
        Nlines = int(Nlines)
        for n in range(0, Nlines):
            print(str(start+n))
            lf.write(str(start+n)+"\n")
        print()
        print("List file '"+fn+"' saved.")
        print (str(os.cwd))
        lf.close()
    else:
        print("There was a problem with your input")
        lf.close()

    
def line():
    for t in range(0,25):
        print("*", end = "")
        time.sleep(0.1)
    print("!")
    return()

main()
