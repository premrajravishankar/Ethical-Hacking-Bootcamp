# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 09:42:34 2021

@author: dell
"""


is_magician =  True
is_expert =  True

# Check if magician and expert
#check if magician but not expert

if is_expert and is_magician:
    print(" You are a master magician!")
    
elif is_magician and not is_expert:
    print(" At least you are getting there!!")
    
elif not is_magician:
    print(" You need magic powers!!")

print(f' {True ==1} \n')
print(1 == '1')    
print('1' is 1)
print(True is True)
print(10 is 10.0)
print('1' is '1')
print([] is [])
