#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 13:18:36 2018

@author: itclunie
"""

#Faster matching b/t lists:-------------------------------------------------
a= [1,2,3,4,5,6,7]
b = [5,6,7,8,9,19]

 for x in a:
     for y in b:
         if x == y:
             print (x,y)
 
print set(a) & set(b) #faster matching