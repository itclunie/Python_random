#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 13:17:51 2018

@author: itclunie
"""

from string import ascii_letters, digits

def ExtractAlphanumeric(InputString):
  return "".join([ch for ch in InputString if ch in (ascii_letters + digits + " '-+.()&:,\/")])