#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 20:41:09 2018

@author: jinyanliu
"""
class Person(object):
     def __init__(self, name):
         self.name = name
    
     def __str__(self):
         return self.name
     
class Student(Person):
    pass

class UG(Student):
    def __init__(self, name,classYear):
        Student.__init__(self, name)
        self.year = classYear
    def getClass(self):
        return self.year
    
    


me = Person('Michael Guttag')
print(me)

p5 = UG("Bily Beaver", 1984)
print(p5, ' is an undergraduate student is ', type(p5) == UG, ' and he will graduate in ', p5.year)