#Set-Location -Path J:\Shared\J6\Constellation\CIIC\Geospatial\Workspace\Clunie\PythonPerl ; C:\Python27\ArcGIS10.2\python.exe "J:\Shared\J6\Constellation\CIIC\Geospatial\Workspace\Clunie\PythonPerl\Python fuzzy match.py"

# C:\Python27\ArcGIS10.2\python.exe \\nnee05s1\cluniei\config\user\cluniei_NGOS.pds\Desktop\deleteme.py
import difflib, sys, keyword

def levenshtein(s1, s2):
    if len(s1) < len(s2):
        return levenshtein(s2, s1)

    # len(s1) >= len(s2)
    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1 # j+1 instead of j since previous_row and current_row are one character longer
            deletions = current_row[j] + 1       # than s2
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
    
    return previous_row[-1]
    
    
a = ["I want it now", "inst", "institute", "isnt of public research", "123",'256346','2364','2423','sdfgf','353','123','isnt of public health']
b = 'isnt of public health'

weighted_results = []
for result in a:
    ratio = difflib.SequenceMatcher(None, result, b).ratio()
    weighted_results.append((result, ratio))

# print weighted_results
print sorted(weighted_results, key=lambda x: x[1])


sys.exit()



outList = sorted(a, key=lambda x: difflib.SequenceMatcher(None, x, b).ratio(), reverse=True)


for item in outList:
    score = levenshtein(b,item)
    if score < len(b):
        print b, item, score
    