# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 20:35:22 2021

@author: dell
"""
user = {
        'name': 'Golem',
        'age': 5006,
        'can_swim': False}

for key, value in user.items():
    print(key, value)
for item in user.values():
    print(item)
for item in user.keys():
    print(item)
for item in user.items():
    print(item)


