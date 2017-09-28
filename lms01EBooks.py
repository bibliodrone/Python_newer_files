# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 18:42:40 2017

@author: walden
"""

import urllib.request as urllib
from bs4 import BeautifulSoup
import re

def TopLevel():
    
    tagList = []
    url = "http://lms01.harvard.edu/ebooks/"
    
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html, "lxml")
    
    tags = soup('a')
    
    for tag in tags:
        tagList.append(url+tag.contents[0])
    tagList.sort()

    print(tagList)

    SecondLevel(tagList)

def SecondLevel(tagList):
    patt=re.compile("([^\.]+)")
    patt2=re.compile("p_m_36.*")
    url=tagList[0]

    print(url)
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html, "lxml")

    #extract the date from the first tag in the table
    tags = soup('a')
    f = tags[0]
    g = f.contents[0]

    print(g)
    h = re.search(patt, g)

    target =""

    #and use date to create URL
    for t in tags:  
        if re.search(patt2,t.contents[0]):
            target=url+"/"+t.contents[0]
            break
    print("Target: ", target)
"""
        elif h:
            print(url + "/" + t.contents[0])
        
    
   
    for tag in tags:
        if re.match(patt, tag.contents[0]):
            regst=str(re.search(patt, tag.contents[0]).group(2))
     """         

       
def main():
    TopLevel()

main()

        
    
