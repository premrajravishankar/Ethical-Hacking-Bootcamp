# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 00:40:09 2021

@author: dell
"""


def test(a):
    '''
    Info: This function tests and prints param a 
    '''
    print(a)
test('!!!!\n \n')
help(test)

print(test.__doc__)

#Clean code
def is_odd_or_even(num):
    if num % 2 ==0:
        return True
    return False
def is_even(num):
    return num %2 ==0
print(is_odd_or_even(50))
print(is_even(12))