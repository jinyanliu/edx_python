#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 18:30:51 2018

@author: jinyanliu
"""

while True:
    val = input("Enter an interger: ")
    try:
        val = int(val)
        print("The square of the number you entered is", val**2)
        break
    except ValueError:
        print(val, "is not an integera")