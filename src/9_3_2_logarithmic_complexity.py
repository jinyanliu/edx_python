#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 11:41:48 2019

@author: jinyanliu
"""
def intToStr(i):
    digits='0123456789'
    if i == 0:
        return '0'
    result = ''
    while i>0:
        x = i%10
        result = digits[x] + result
        i = i//10
    return result

print (intToStr(25))

def addDigits(n):
    stringRep = intToStr(n)
    val = 0
    for c in stringRep:
        val += int(c)
    return val

print (addDigits(25))

print (2**20)