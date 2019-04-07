#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 12:16:45 2018

@author: jinyanliu
"""

s= "1.23, 2.4, 3.123"

sArray = s.split(',')

total = 0

for sString in sArray:
    total = total + float(sString)
    
print(total)