# -*- coding: utf-8 -*-

import os, csv, time, datetime, sys
from os import stat

counter = 0

def find_owner(filename):
    return getpwuid(stat(filename).st_uid).pw_name

def main(folder, outputfile):
    with open(outputfile, "wb") as f:
        w = csv.writer(f)
        header = ("Name/type", "Path", "Size KB","lastmod","owner","count")
        w.writerow(header)
        rows = crawlfiles(folder)
        w.writerows(rows)

def crawlfiles(folder):
    for root, dirs, files in os.walk(folder):
        for f in files:
            try:
                filePath = os.path.join(root, f)
                filePath2 = os.path.join(root) #without extension
                filetype = os.path.basename(filePath)
                fileName = os.path.splitext(f)[0]
                fileSize = os.path.getsize(filePath) / 1000
                lastmod = time.strftime('%Y-%m-%d %H:%M', time.gmtime(os.path.getmtime(filePath)))

                owner = os.stat(filePath)

                #counter += 1
                #print(counter)
   
                seq = (filetype,filePath2,fileSize,lastmod,owner)#,counter)
                yield seq
            except:
                pass
            
if __name__ == "__main__":
    folderPath = r"\\nnee05s1\cluniei\config\user\cluniei_NGOS.pds\Desktop\VM" # or arcpy.GetParameterAsText(0)
    #folderPath = r"J:\Shared\J2-5-8R\J20\CIIC" # or arcpy.GetParameterAsText(0)
    output = r"\\nnee05s1\cluniei\config\user\cluniei_NGOS.pds\Desktop\test.csv" # or arcpy.GetParameterAsText(1)
    main(folderPath, output)


