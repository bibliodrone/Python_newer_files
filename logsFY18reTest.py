# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 19:22:43 2017

@author: walden
"""
import re

logs_list = ["kanopy20170526.zero.m18.doc_log",
"p_m_36.kanopy20170526.log",
"kanopy20170106.one.hol.one.m18.doc_log",
"kanopy20170106.zero.m18.doc_log",
"p_m_36.kanopy20170106.log",
"kanopy20160810.one.hol.one.m18.doc_log",
"kanopy20160810.zero.m18.doc_log",
"p_m_36.kanopy20160810.log"]

date = re.compile("(201[0-9]+[^.])")

for i in logs_list:
    print(re.search(date, i))