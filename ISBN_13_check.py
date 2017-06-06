#ISBN_13_check.py
#Calculates the check digit for a 13-digit ISBN.
#There are two examples hard-coded for testing, but
#the input could be provided by a user. 

import re

def isbn_check(ISBN):

    print("Let's see if",ISBN,"is a valid ISBN.")

    #Pull out the non-digit parts and join up what remains
    ISBN = ''.join(c for c in ISBN if c.isdigit())

    #Error-checking; should now be 13 digits as input.
    if len(ISBN)!= 13:
        print('Please enter 13 digits!')
    else:
        print("Calculating")

        total = 0
        mod = 0
        for n in range (0,12): #1st, 3rd, etc. mult. by 3; 2nd, 4th etc. by 1
            if n%2 != 0:
                print (ISBN[n] + "* 3")
                total = total + (int(ISBN[n]) * 3)
            else:
                print(ISBN[n] + "* 1")
                total = total + (int(ISBN[n]))
        print("Total is " + str(total))
        mod = total % 10
        print(str(total) + " mod 10 is " + str(mod))
        chk = 10-mod
        
        print("The check digit should be", str(chk))
        print("Your number is", str(ISBN[12]))
        if str(ISBN[12]) != str(chk):
            print("Your ISBN doesn't seem to be valid.\n\n")
        else:
            print("Looks valid.\n\n")
    
def main():
    isbn1 = "978-0-306-406157"
    isbn2 = "978-0-306-406155"

    #ISBN = input('Please enter a 13-digit ISBN')
    print ("First time: ")
    isbn_check(isbn1)
    print ("Second time: ")
    isbn_check(isbn2)    
    
main() #After defining main(), have to be sure to actually call it. 
