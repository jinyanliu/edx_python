#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 18:14:20 2018

@author: jinyanliu
"""



def sumDigits(s):
    
    sum = 0
    for i in s:
        try:
            sum = sum + int(i)
        except ValueError:
            continue
    print(sum)
    
    
sumDigits("a2b3c")
        