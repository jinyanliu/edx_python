#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 15:51:39 2018

@author: jinyanliu
"""

L1 = [1,28,36,0]
L2 = [2,57,9,9,9,0,7,6]
for i in map(min, L1, L2):
    print(i)