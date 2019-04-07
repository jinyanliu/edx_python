#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 13:03:32 2018

@author: jinyanliu
"""

nameHandle = open('kids','w')
for i in range(2):
    name = input('Enter name: ')
    nameHandle.write(name +'\n')
nameHandle.close()