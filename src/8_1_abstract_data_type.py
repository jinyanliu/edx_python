#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 13:50:44 2018

@author: jinyanliu
"""

class IntSet(object):
    
    def __init__(self):
        self.vals = []
        
    def insert(self,e):
        if e not in self.vals:
            self.vals.append(e)
            
    def __str__(self):
        self.vals.sort()
        result = ""
        for e in self.vals:
            result =result + str(e) + ','
        return '{' +result[:-1] + '}'
            
            

myIntSet = IntSet()
myIntSet.insert(4)
IntSet.insert(myIntSet, 6)
print(myIntSet)

print (myIntSet.__str__())
print (IntSet.__str__(myIntSet))


print(str(myIntSet))

print(hash(myIntSet))
print()

myIntSet.insert(8)

print(hash(myIntSet))
