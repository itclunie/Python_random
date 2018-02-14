import urllib2, re, csv, os, sys, time

#crawl part
url = 'http://analystcave.com/vba-cheat-sheet/'
response = urllib2.urlopen(url)
htmlText = response.read()


matchedList = []     

#regex part, fill list with matches
matchedList = []     # regex matches all content between character <img src= and "\s  (\s = space) in the html
for m in re.finditer('<img src="(.*?)"\s',htmlText, re.MULTILINE|re.IGNORECASE|re.DOTALL):
	matchedList.append(m.group(1))

# sys.exit()
#create empty csv (if csv with same name exists, overwrites), insert headers
csvOutput = os.path.abspath('J:\Shared\J6\Constellation\CIIC\Geospatial\Workspace\Clunie\python_crawl_demo\Image crawler CSV.csv')

csvHeaders = ['Image url','number']

with open(csvOutput, 'w') as output:
	writer = csv.writer(output, lineterminator = '\n')
    writer.writerows([csvHeaders])

	
#fill CSV with image urls
countr = 0
with open(csvOutput, 'a') as output:
	writer = csv.writer(output, lineterminator = '\n')
	
	for image in matchedList:
		print image
		countr += 1
		tempList = [image,countr]
		writer.writerows([tempList])
	
#-------------------------------------------------------------------------------------continuous stock price crawler

# started here http://data.cnbc.com/quotes/.SPX but instead of using/scraping the html, looked for a GET request that used json. Cleaner/faster
def getprice():
	url = 'http://quote.cnbc.com/quote-html-webservice/quote.htm?callback=webQuoteRequest&symbols=.SPX&symbolType=symbol&requestMethod=quick&exthrs=1&extMode=&fund=1&entitlement=0&skipcache=&extendedMask=1&partnerId=2&output=jsonp&noform=1'
	response = urllib2.urlopen(url)
	htmlText = response.read()
	SandPprice = re.search('"last":"(.*?)","curmktstatus',htmlText, re.MULTILINE|re.IGNORECASE|re.DOTALL)
	print SandPprice.group(1)

LoopScript = True
while LoopScript == True:
	getprice()
	time.sleep(.5)	