#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 13:11:28 2018

@author: itclunie
"""

import arcpy, os, timeit, time, sys, csv, urllib2 , zipfile, shutil, inspect, random, string

#1------------------------------return list name not contens------------------------------------------------------------------
def returnName(var):
    localvars = inspect.currentframe().f_back.f_locals.items()
    return[var_name for var_name, var_val in localvars if var_val is var]

for name in listNames:
    holder = returnName(name) 
    if holder[0] != 'name':
        csvNames.append(holder[0])
        csvnamePath = os.path.abspath("CSVs\\" + holder[0] + ".csv")
        csvnamePathLst.append(csvnamePath)
    elif holder[1] != 'name':
        csvNames.append(holder[1])
        csvnamePath = os.path.abspath("CSVs\\" + holder[1] + ".csv")
        csvnamePathLst.append(csvnamePath)
        

#3------------------------------create log file------------------------------------------------------------------
#write all prints to text file too
startdatetime = time.asctime(time.localtime(time.time()))
startdatetime = startdatetime.replace(":",".")
report = open(os.path.abspath('reportfile_' + startdatetime + ".txt" ),'w')

tic = timeit.default_timer() #timing how long process takes. timer start
#stuff happends
toc = timeit.default_timer()
t1 = toc - tic
report.write("made view processes " + str(round((t1/60),2)) + " minutes" + '\n')


#5------------------------------download & chunkify--------------------------------------------------------------------------
def downloadlargefile(url,unzip):
    url = 'https://balhablahblah.com
    response = urllib2.urlopen(url)
    CHUNK = 16 * 1024

    with open(unzip,'wb') as f:
        while True:
            chunk = response.read(CHUNK)
            if not chunk: break
            f.write(chunk)
            
    #put folder name b/t the () to extract to this folder/gdb
    with zipfile.ZipFile(unzip, 'r') as z:
        z.extractall()