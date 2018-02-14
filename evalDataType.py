#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 13:18:13 2018

@author: itclunie
"""

#Eval-------------------------------------------------------------
testr = ['abc','aaa','qrq']
for item in testr:
    eval(compile("if 'aaa' in '" + item + "': tmp = 'y'", '<string>', 'exec'))
    if tmp == 'y': print 't'
    else: print 'f'
        
    tmp = ''