#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 13:17:58 2018

@author: itclunie
"""

#json prettyprint-------------------------------------------------------------------
import json
jsonpath = r'J:\Shared\whatever\rawjson.js'
parsed = json.load(jsonpath)
formatted = json.dumps(parsed, indents=4,sort_keys=True)
Then you can just write the 'formatted' string to a text file.