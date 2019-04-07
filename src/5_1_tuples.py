#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 19:34:08 2018

@author: jinyanliu
"""

t1 = (1, 'two', 3,)
print(t1)
t2 = (t1, 3.25,1,3)

def intersect(t1, t2):
    result = ()
    for e in t1:
        if e in t2:
            result += (e,)
    return result

print(intersect(t1, t2))

t3= 3*('two',2)
print(t3)