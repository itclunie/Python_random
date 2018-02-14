#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 13:12:13 2018

@author: itclunie
"""

import arcpy, os, timeit, time, sys, csv, urllib2 , zipfile, shutil, inspect, random, string


#2------------------------------list contents 2 csv------------------------------------------------------------------
def conserveMemory(list_of_lists, csvPathsList):
#takes stuff being added to list, dumps list contents into csv, empties list
    counnter = 0
    for i in range(len(csvPathsList)):
        with open(csvPathsList[i], 'a') as output:
            writer = csv.writer(output, lineterminator = '\n')

            for item in list_of_lists[i]:
                writer.writerows([item])
        output.close()
        
    for lisst in list_of_lists:
        lisst[:] = []

test1 = []
test2 = []
test3 = []
listNames = [test1,test2,test3]

rowcounterz = 0
rowcounter = 0
with arcpy.da.SearchCursor(Output_Layer, Fieldz) as cursor:
    for row in cursor:
        
        if rowcounterz == 10000:
            conserveMemory(listNames, csvnamePathLst) 
            rowcounterz = 0
            print rowcounter

        if row[34] != 'I':
            coord = row[6]
            Extended = []
            Extended = coordconverter(coord) #my cord DMS to decimal converter
            Appended = []
            
            for f in range(len(Fieldz)):
                Appended.append(row[f])
            Appended.append(Extended[0])
            Appended.append(Extended[1])

            if row[1] == 'blah':
                MIDB_CHEM_BIO_ALL.append(Appended)
            if row[2] == 'blah2':
                MIDB_PROD_CHEM.append(Appended)
            if row[3] == 'blah3':
                MIDB_INFRA_DENTAL.append(Appended)
            #etc...
                
        rowcounterz += 1
        rowcounter += 1

conserveMemory(listNames, csvnamePathLst)