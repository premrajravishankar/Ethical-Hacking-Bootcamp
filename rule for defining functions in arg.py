# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 01:26:57 2021

@author: dell
"""

# *args **kwargs(keyword args)
def super_func(name,*args, i='hi', **kwargs):
    total = 0
    for items in kwargs.values():
        total += items
    print(*args)
    print(kwargs)
    print(args)
    return total
    # return sum(args)+sum(items in kwargs)
print(super_func('ravi',1,2,3,4,5, num1=5,num2=10))

#Rule: params, *args, default parameters, **kwargs
