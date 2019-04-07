#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 13:44:52 2019

@author: jinyanliu
"""

L = [[1, 2, 3], (3, 2, 1, 0), 'abc']
print(sorted(L, key=len, reverse=True))

L = [1, 2, 6, 5]
print(sorted(L))

L = [1, 'b', 2, 6, 5, 'a']
print(sorted(L))
