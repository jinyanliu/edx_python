#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 14:54:29 2018

@author: jinyanliu
"""

nameHandle = open('kids', 'w')
nameHandle.write("s\nr\nd\n")
nameHandle.close()

nameHandle = open('kids', 'r')
print(nameHandle.readlines())
nameHandle.close()