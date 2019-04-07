#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 19:12:05 2018

@author: jinyanliu
"""

epsilon = 0.01
k = 0
numGuesses = 0

low = min(k, 0.0)
high = max(1.0, k)


guess = (high + low)/2.0
while abs(guess**3 -k) >= epsilon:
    guess = guess -(((guess**3)-k)/(3*guess**2))
    numGuesses +=1
print('numGuesses =', numGuesses)
print('Square root of', k, 'is about', guess)