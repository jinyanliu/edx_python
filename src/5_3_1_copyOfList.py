#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 13:52:10 2018

@author: jinyanliu
"""
import copy



l = [9,10]
L1 = [1,2,5,l]

l.append(11)

L2 = copy.copy(L1)
L3 = copy.deepcopy(L1)

l.append(12)

print('L2 =', L2)
print('L3 =', L3)

        



