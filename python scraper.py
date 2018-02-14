
import urllib2

file = "C:\Users\cluniei\Downloads\downloaded_file.xlsx"

url = "http://www.arcgis.com/sharing/rest/content/items/8376f3ca83ce4bc3b59f4c9d98fd862c/data?token=M-g7OrPG3UXYmw2-fTfoBjphRD-hpODIvWe4QGxHYzpDLEyFRkM_NtDGFx7EU03O6BfWfdtMfowGVLX1846mJbA1yK0w7BENOhcX79GmPEX2ysgSNxLPZHQCMkm5a8esMdsqZxrZC7YzeOyItO0RcQ"
req = urllib2.Request(url)
response = urllib2.urlopen(req)

#open the file for writing
fh = open(file,'wb')

# read from request while writing to file
fh.write(response.read())
fh.close()
