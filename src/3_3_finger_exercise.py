#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 12:23:59 2018

@author: jinyanliu
"""

x= 0
epsilon = 0.01
numGuesses = 0
low = min(x, 0.0)
high = max(1.0, x)
ans = (high + low)/2.0
while abs(ans**3-x)>= epsilon:
    print('low =', low, 'high =', high, 'ans =', ans)
    numGuesses +=1
    if ans**3 <x:
        low = ans
    else:
        high = ans
    ans = (high +low)/2.0
print('numGuesses =', numGuesses)
print(ans, 'is close to square root of', x)