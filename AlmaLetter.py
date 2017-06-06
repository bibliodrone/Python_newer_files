# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 17:33:42 2017

@author: walden
"""

from lxml import etree

fname = "AlmaClaim.txt"

with open(fname, 'r', encoding='utf-8') as fn:
    tree=etree.parse(fn)
    
etree.tostring(tree)
    