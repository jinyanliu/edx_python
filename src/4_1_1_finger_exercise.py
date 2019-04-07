#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 11:23:30 2018

@author: jinyanliu
"""

x = "adfhakjdhfaklhdjka"
y = "hak"


def isIn(x,y):
    if x in y or y in x:
        return True
    else:
        return False


result = isIn(x,y)
if(result):
    print("True")
else:
    print("False")



    