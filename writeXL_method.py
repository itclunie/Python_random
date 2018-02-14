import xlwt


def writeXL_method(inputList,SheetName,WorkbookName):
    checkLen = 0
    
    workbook = xlwt.Workbook()                #Add an excel workbook
    worksheet = workbook.add_sheet(SheetName) #Add an excel sheet

    for x in range(len(inputList)):               #number of cols
        for y in range(len(inputList[checkLen])): #number of rows, inputList[checkLen] returns the length of each col
            worksheet.write(y, x, inputList[x][y]) 

        checkLen += 1

    workbook.save(WorkbookName + '.xls')


###*******test
##from readXL_methods import readXL_method1
##from readXL_methods import readXL_method2
##import os
##
##csvlist1 = ['header1','a2','a3', 'a4']
##csvlist2 = ['header2','b2','b3', 'b4']
##csvlist3 = ['header3','c2','c3']
##toplist = [csvlist1,csvlist2,csvlist3]
##
##dataout = readXL_method1(r"J:\Shared\J6\Constellation\CIIC\Geospatial\Workspace\Clunie\PythonPerl\Lessons\Lesson 4\InputWorkbook.xls",'Sheet1')
##
##writeXL_List2XL(dataout,'Sheet1','List2XL')

