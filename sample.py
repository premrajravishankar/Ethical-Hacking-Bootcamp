# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 04:04:24 2021

@author: dell
"""


my_tuple = (1,2,3,4,5,5,6,5)
print(5 in my_tuple)
user = {
        (1,2) : [1,2,3],
        'greet': 'hello',
        'age': 20
        }
print(user['greet'])
print(user.items()) 
print(user[(1,2)])
new_tuple =my_tuple[1:2]
x= my_tuple[0]
y,z,*other = my_tuple
print(other)
print(my_tuple.index(5))
print(my_tuple.count(5))
print(len(my_tuple))

my_list = [1,2,3,4,5,5]
my_set = {1,2,3,4,5,5}
my_set.add(100)
my_set.add(2)
print(my_set)
print(my_list)
print(set(my_list))
print(1 in my_set) 
print(len(my_set))
new_set = my_set.copy()
print(new_set)
my_set.clear()
print(my_set)
