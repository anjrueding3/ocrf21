import jpg2data
from openpyxl import load_workbook, Workbook

objectList = jpg2data.read2Data('/Users/andrewding/Desktop/ocrF21/src/assets/extracted')

# def updateExcel(objectList, targetExcel):
#     workbook = load_workbook(targetExcel)
#     sheet = workbook.active

#     maxRow = sheet.max_row
    
#     for object in objectList:

#         matchFound = False

#         for i in range(maxRow):
#             actualCell = i + 1
#             actualIHD = 'A' + str(actualCell)
#             actualPO = 'B' + str(actualCell)
#             actualStyle = 'C' + str(actualCell)

    
#             if object.getPO() == sheet[actualPO].value:
#                 matchFound == True
#                 print('replacing ' + str(sheet[actualIHD].value) + ' with ' + object.getIHD())
#                 sheet[actualIHD] = object.getIHD()
#                 print('replacing ' + str(sheet[actualStyle].value) + ' with ' + object.getStyle())
#                 sheet[actualStyle] = object.getStyle()
#                 break
                

#         if matchFound == False:
#             nextEmptyCell = maxRow + 1
#             emptyIHD = 'A' + str(nextEmptyCell)
#             emptyPO = 'B' + str(nextEmptyCell)
#             emptyStyle = 'C' + str(nextEmptyCell)
#             sheet[emptyIHD] = object.getIHD()
#             sheet[emptyPO] = object.getPO()
#             sheet[emptyStyle] = object.getStyle()
#             maxRow += 1


    
#     workbook.save(filename= targetExcel)


    #for object in objectList:
        #object.getInfo()
    

def updateExcel(objectList, targetExcel):
    workbook = load_workbook(targetExcel)
    sheet = workbook.active
    maxRow = sheet.max_row
    
    for object in objectList:
        matchFound = False

        #match object.PO() to Cell B(of row Num) until there's a match
        for i in range(maxRow):
            #start from A1, B1, C1
            actualRow = i + 1
            actualIHD = 'A' + str(actualRow)
            actualPO = 'B' + str(actualRow)
            actualStyle = 'C' + str(actualRow)
            
            if object.getPO() == sheet[actualPO].value:
                sheet[actualIHD] = object.getIHD()
                sheet[actualStyle] = object.getStyle()
                matchFound = True
                break
        
        if matchFound == False:
            sheet.append([object.getIHD(), object.getPO(), object.getStyle()])
            maxRow += 1



    workbook.save(filename= targetExcel)






updateExcel(objectList, '/Users/andrewding/Desktop/targetExcel.xlsx')

# targetExcelFile = /Users/andrewding/Desktop/targetExcel.xlsx