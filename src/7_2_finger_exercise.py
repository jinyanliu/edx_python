#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 09:44:00 2018

@author: jinyanliu
"""

def findAnEven(L):
    for i in L :
        if i % 2 == 0:
            return i
    raise ValueError ("L does not contain an even number")
    


print(findAnEven([1,3,7,9,2]))