# Re-format XML (.txt file) of an Aleph vendor letter to determine what fields are used, and which are not

import re

def main():
    
    doc = "Aleph48792.txt"
    lengthOut = 250
    readLetter(doc, lengthOut) #filename, max lines to print
  
def readLetter(doc,lengthOut):
    
    pattern = re.compile("^(\<.+\>)(.+)(\<.+\>)") #get tags and innerHTML in groups
    counter=0
    counter_x=0
    emptyFields=[]

    hdr1 = "Tag".center(35,"-")
    hdr2 = "Text".center(40,"-")

    print(hdr1, hdr2)

    
    with open(doc, 'r', encoding = 'utf-8') as readfile: #specify encoding for proper diacritics display

        for line in readfile:    
            if len(line.strip())< 1:
                print("", end = "")
                
            elif re.search(pattern, line): #line has tags containing text values.
                counter +=1
                if counter < lengthOut: 
                    grp1 =re.search(pattern, line).group(1).ljust(35) #tag
                    grp2 =re.search(pattern, line).group(2)  #text
                    if len(grp2)> 40:
                        grp2 = grp2[:40]+" [...]" #abbreviate long lines to 40 chars
                    st1=(str(counter)).ljust(4)
                    print(st1,grp1,grp2,end = "\n")
                    
            else:
                counter_x +=1
                emptyFields.append(str(line))
                #if counter_x < 11:
                #    print("Empty field", counter_x,":",line, end="\n")

    letterStats(counter, counter_x, emptyFields)
            
def letterStats (counter, counter_x, emptyFields):
    print("\nPattern-matching lines:", counter)
    print("Non-pattern-matching lines:", counter_x)

    empties = len(emptyFields)

    print("\n" + str(empties), "empty fields recovered, including ", end="")

    emptySet = set(emptyFields)
    uniques = len(emptySet)

    print(str(uniques), "unique empty fields.")


main()
        
    
       
        





    
