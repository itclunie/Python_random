#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 13:17:43 2018

@author: itclunie
"""

#numpy & map------------------------------------------------------------------------
import numpy as np
import array
def d2s(list):
    # 'digits to string
    return array.array('B', list).tostring()
def s2d(string):
    # 'string to digits
    return map(ord, string)
def npAry(listOdigits):
    return np.array(listOdigits, int)
    
strList = ['a', 'bob', 'cat', 'b'] #list of strings
digitList = map(s2d, strList)      #convert to digits
# reStrLst = map(d2s, digitList)       #back to strings
a = map(npAry,digitList) #put into numpy array
reStrLst = map(d2s, a)
print reStrLst
for item in a:
    print item
	
	
#-----------------------------------------------------------like map func
def isMp3(s):
    if s.find(".mp3") == -1:
        return False
    else:
        return True
 
list = ["1.mp3","2.txt", "3.mp3", "4.wmv","5.mp4" ]
temp = filter(isMp3,list)
 
for item in temp:
    print item