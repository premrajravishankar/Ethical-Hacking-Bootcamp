# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 00:18:13 2021

@author: dell
"""


def sum(num1, num2):
    def another_func(n1, n2):
        return n1+n2
    return another_func(num1, num2)
    print('hello')
    return 5
#Should do one thing really well
#Should return something


print(sum(10,sum(5,6)))
