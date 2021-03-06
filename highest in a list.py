# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 09:30:51 2021

@author: dell
"""

# def highest_even(li):
#     highest=li[0]
#     for i in li:
#         if i>highest:
#             if i%2 ==0:
#                 highest =i
#     return highest
# print(highest_even([10,2,3,4,8,11,12]))
def highest_even(li):
    evens = []
    for i in li:
        if i%2 ==0:
            evens.append(i)
    return max(evens)
print(highest_even([10,2,3,4,8,11]))
