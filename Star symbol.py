# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 00:29:56 2021

@author: dell
"""


#Exercise!
#Display the image below to the right hand side where the 0 is going to be ' ', and the 1 is going to be '*'. This will reveal an image!
picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]


        
for image in picture:
    string=''
    for pixel in image:
        if (pixel == 1):
            print('*', end = '')
            
        else:
            print(' ', end= '')
    print('\n')
    
    
    
    
# iterate over picture1
    # if  0 -> print ' ' :
    # if  1  -> print '*'