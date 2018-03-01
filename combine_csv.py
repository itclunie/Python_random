pathList = []
for filename in os.listdir(os.getcwd()):
    if '.csv' in filename and not 'combined.csv' in filename:
        pathList.append(os.getcwd() + "\\" + filename)

#grab headers
with open(pathList[0], 'r') as output:
    reader = csv.reader(output, lineterminator = '\n')
    row1 = next(reader)

outputCSV = str(os.getcwd()) + "\\combined.csv"

#write headers
with open(outputCSV, 'w') as outputWrite:
    writer = csv.writer(outputWrite, lineterminator = '\n')
    writer.writerows([row1])

with open(outputCSV, 'a') as outputWrite:
    writer = csv.writer(outputWrite, lineterminator = '\n')

    for csvpath in pathList:
        with open(csvpath, 'r') as output:
            reader = csv.reader(output, lineterminator = '\n')
            reader.next()
            
            for row in reader:
                writer.writerows([row])
