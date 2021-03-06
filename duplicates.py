# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 22:49:37 2021

@author: dell
"""


       
some_list = ['a','b','c','b','d','m','n','n']
duplicates=[]
check = []
# for i in some_list:
#     if i not in check:
#         check.append(i)
#     elif i in check:
#         duplicates.append(i)
# print(duplicates)
        
for value in some_list:
    if some_list.count(value)>1:
        if value not in duplicates:
            duplicates.append(value)
print(duplicates)        