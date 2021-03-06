# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 21:11:04 2021

@author: dell
"""




print('Please Think of a number betweeen 0 and 100!')
high=100
low =0
Try = 0
print('Is your secret number ', int((high+low)/2), '?')
c = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
while True:    
    if Try == 1:
        if c == 'l':
            low = int((high+low)/2)
            print('Is your secret number ', low, '?')
            c = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
        elif c == 'h':
            high = int((high+low)/2)
            print('Is your secret number ', high, '?')
            c = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
        elif c == 'c':
            print('Game over. Your secret number was: ', int((high+low)/2))
            break
        else:
            print('Sorry, I did not understand your input.')
            print('Is your secret number ', int((high+low)/2), '?')
            c = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
        
    else:
        if c == 'h':
            Try = 1
            high = int((high+low)/2)
        if c == 'l':
            Try = 1
            low = int((high+low)/2)
        elif c == 'c':
            print('Game over. Your secret number was: ', int((high+low)/2))
            break