import xlrd


def readXL_method1(XL_location,sheet_name):
    workbook = xlrd.open_workbook(XL_location)
    sheet1 = workbook.sheet_by_name(sheet_name)
##    sheet1 = workbook.sheet_by_index(sheet_index)
    data = []
    colList = []
    rowCount = 0
    colCount = 0
    cellCount = 0

    total_cells = sheet1.ncols * sheet1.nrows
    
    while cellCount != total_cells:     
        cellCount += 1
        
        cellvalue = sheet1.cell_value(rowCount,colCount)
        colList.append(cellvalue)

        rowCount += 1
        
        if rowCount == sheet1.nrows:
            colCount += 1
            rowCount = 0
            data.append(colList)
            colList = []
        if colCount == sheet1.ncols:
            colCount = 0
            
    return data


def readXL_method2(XL_location,sheet_name):
    #read excel file (filename at the moment is Sample.xls)
    workbook = xlrd.open_workbook(XL_location)
    #read content of Sheet1
    sheet = workbook.sheet_by_name(sheet_name)

    allInfo = [] #nested list for row and column data

    for rows in range(sheet.nrows):    
            current = [] #list for row data
            for cols in range(sheet.ncols):
                #add information to the list
                current.append( sheet.cell_value(rows,cols) )
            #add list to the nested list
            allInfo.append(current)

    return allInfo

###*******test
##file_location = r"\\nnee05s1\cluniei\config\user\cluniei_NGOS.pds\Desktop\Lesson 4\InputWorkbook.xlsx"
##
##dataout = readXLdata(file_location,'Sheet1')
##
##for item in dataout:
##    print item
