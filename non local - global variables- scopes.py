# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 09:55:07 2021

@author: dell
"""


total = 0
def count(total):
    '''
    

    Parameters
    ----------
    total : TYPE
        global total.

    Returns
    -------
    total : TYPE
        Value incremented locally by 1.

    '''
    total += 1
    return total
count(total)
count(total)
print(count(total))
print(count(count(count(total))))
print(total)

def outer ():
    x = 'local'
    def inner():
        # non local x because to avoid using extra space
        nonlocal x
        x = "nonlocal"
        print("inner  : ", x)
    inner()
    print("outer : ", x)
outer()

# 1 - start with locals
# 2 - parent local?
# 3 - globals
# 4 - non local