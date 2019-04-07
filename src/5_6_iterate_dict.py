#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 17:33:48 2018

@author: jinyanliu
"""
empty={}
monthNumbers = {2:'Feb', 'Jan':1, 'Feb':2, 'Mar':3, 'Apr':4, 'May':5,
                1:'Jan', 3:'Mar', 4:'Apr', 5:'May'}
keys = []
for e in monthNumbers:
    keys.append(str(e))
print(keys)
keys.sort()
print(keys)

keys2 = []
for e in empty:
    keys2.append(str(e))
print(keys2)
keys2.sort()
print(keys2)

print(monthNumbers.keys())
print(monthNumbers.values())

print(empty.keys())
print(empty.values())

print(monthNumbers[3])

print(len(monthNumbers))
print(len(empty))

print(empty.get(1,2))
print(monthNumbers.get(1,2))

empty[2] = 5
monthNumbers[2] = 5

print(empty.values())
print(monthNumbers.values())

print(empty.keys())
print(monthNumbers.keys())

del empty[2]
del monthNumbers[2]

print(empty.values())
print(monthNumbers.values())

print(empty.keys())
print(monthNumbers.keys())