# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 23:14:30 2021

@author: dell
"""


for i,char in enumerate((1,2,3)):
    print(i, char)

for i,char in enumerate('Helloo'):
    print(i, char)

for i,char in enumerate(list(range(100))):
    if char == 50:
        print(f'The index of 50 is {i}')
        
i= 0
while i<50:
    print(i)
    i += 1
else:
    print('Done with all the work!!')

i=0
my_list = [4,5,6]
while i < len(my_list):
    print(my_list[i])
    i+=1


while True:
    response = input('say something: ')
    if response == 'bye':
        break