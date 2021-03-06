# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 23:02:06 2021

@author: dell
"""

# parameters
# positional parameters
def say_hello(name='Darth Vader', emoji='😒'):
    print(f'Hello {name}!! {emoji}')

#positional arguments    
say_hello('Ravi Shankar', '😊')  #invoking function
say_hello('Dan', '😍')
say_hello('Ajay', '🤦‍♂️')

# keyword arguments
say_hello(emoji='😁', name='Latha')

#default parameters -arguments
say_hello()
say_hello('Timmothy')