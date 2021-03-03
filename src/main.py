#! python3

import pdf2jpg as convert
import extractPDF
import jpg2data
import updateExcel
import os, sys

# 1. convert.directory_to_jpeg(/f21_pdfs)

# 2. now we have a convertedPDFS folder full of this runs pdfs

# 3. go through the list of files, extract ihd, po and style. How should i organize the extracted data?

# 4. Looks like i'm going to store each package of data in it's own directory within './assets/extracted'. Name directory filename + 'Data.

# 5. Need to remember to have an automated clear all assets, extracted, f21 pdfs, and converted pdfs function once i've confirmed everything is chillin.


#NOTES:
# Absolutely need my assets to look like this -->>  /Users/andrewding/Desktop/ocrF21/src/assets/extracted/21008188'
# Need to think of potential bugs


##### PROGRAM FLOW ######

# 1. Pass in PDF Directory, convert to 'convertedPDFs' Folder

if len(sys.argv) < 2:
    print('Usage: Add source PDF folder and target Excel file. 3 Args')
    sys.exit()


sourcePDF = sys.argv[1]
targetExcel = sys.argv[2]
convertedImageFolder = os.getcwd() + '/assets/convertedPDFs'
extractedFolders = os.getcwd() + '/assets/extracted'


convert.directory_to_jpeg(sourcePDF)


#2. directory to pass into extract_directory_data()
#imageFolder = os.getcwd() + '/src/assets/convertedPDFs'
extractPDF.extract_directory_data(convertedImageFolder)


#3. Convert every individual order data folder in 'extracted' into a text, pass into object. Create new class readFromExtracted
#import jpg2data
objectList = jpg2data.read2Data(extractedFolders)
##for data in objectList:
    #print(data.getPO())


#4 Now I have the object list. Time to extract data into excel file.

updateExcel.updateExcel(objectList, targetExcel)


#src/assets/extracted/21002546




