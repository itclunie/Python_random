#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 13:18:05 2018

@author: itclunie
"""

#iterate over dates----------------------------------------------------------
from datetime import timedelta, date
def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)
start_date = date(2013, 1, 1)
end_date = date(2015, 6, 2)
for single_date in daterange(start_date, end_date):
    print single_date.strftime("%Y,%m,%d")
