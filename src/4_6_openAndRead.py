#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 14:43:48 2018

@author: jinyanliu
"""

nameHandle = open('kids', 'r')
for line in nameHandle:
    print(line)
nameHandle.close()