# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 09:41:32 2021

@author: dell
"""


# Scope - What variables do I have access to?

a = 1
def parent():
    a=10
    def confusion():
        return sum
    def confusion2():
        print(a)
    confusion2()    
    return confusion()
print(parent())
print (a)
