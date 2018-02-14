import urllib, urllib2, os, sys, json

#google how to encode text files with utf-8 so itll write stuff like $




#steps
#1. regex to find the __VIEWSTATE, __VIEWSTATEGENERATOR, etc values in the html of https://www.bikereg.com/events/Road-Race/
	#-note some youll fill yourself like  ctl00$ContentPlaceHolder1$txtZip = "22206"
#2. create json with values youve found
#3. run post/request
#4. use regex to grab values you want out of your 2nd html page
#5. store values 

url = 'https://www.bikereg.com/events/Road-Race/'

a = [r'ctl00_JScripts1_ScriptManager1_TSM', ...]
b = [r'__VIEWSTATE', ...
c = [r'__VIEWSTATEGENERATOR',"50DF723F"]
d = [r'__PREVIOUSPAGE',...
e = [r'ctl00$navMenu1$DropDownListUserType',"l"]
f = [r'page_is_dirty',"-1"]
g = [r'ctl00$ContentPlaceHolder1$cboType',"1"]
h = [r'ctl00$ContentPlaceHolder1$numMiles',"50"]
i = [r'ctl00_ContentPlaceHolder1_numMiles_ClientState',"""{"enabled":true,"emptyMessage":"miles","validationText":"50","valueAsString":"50","minValue":-70368744177664,"maxValue":70368744177664}"""]
j = [r'ctl00$ContentPlaceHolder1$txtZip',"22206"]
k = [r'ctl00$ContentPlaceHolder1$btnSearch',"Search"]
l = [r'ctl00$ContentPlaceHolder1$hiddenCurrentPage',"1"]
m = [r'ctl00$ContentPlaceHolder1$hiddenLastPage',"7"]
n = [r'ctl00$ContentPlaceHolder1$hfregionID',"0"]
o = [r'ctl00$ContentPlaceHolder1$hfpromoterID',"-1"]
p = [r'ctl00$ContentPlaceHolder1$hfdistance',"99999"]
q = [r'ctl00$ContentPlaceHolder1$hfResultcount',"93"]
r = [r'ctl00$ContentPlaceHolder1$hfTypeList',"1"]
s = [r'hiddenInputToUpdateATBuffer_CommonToolkitScripts',"1"]

# sys.exit()

data = urllib.urlencode({
	a[0]:a[1],b[0]:b[1],c[0]:c[1],d[0]:d[1],e[0]:e[1],f[0]:f[1],g[0]:g[1],h[0]:h[1],i[0]:i[1],
	j[0]:j[1],k[0]:k[1],l[0]:l[1],m[0]:m[1],n[0]:n[1],o[0]:o[1],p[0]:p[1],q[0]:q[1],r[0]:r[1],s[0]:s[1]
	})


req = urllib2.Request(url, data)

response = urllib2.urlopen(req)

htmlText = response.read()

# text_path = os.path.abspath(r'J:\Shared\J6\Constellation\CIIC\Geospatial\Workspace\Clunie\python_crawl_demo\bikePOST.html')
# text_file = open(text_path, "w")
# text_file.write(response.read())


