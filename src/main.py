import pdf2jpg as convert
import extractPDF
import jpg2data
import os

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
#convert.directory_to_jpeg('/Users/andrewding/Desktop/ocrF21/src/assets/f21_pdfs')


#2. directory to pass into extract_directory_data()
#imageFolder = os.getcwd() + '/src/assets/convertedPDFs'
#extractPDF.extract_directory_data(imageFolder)


#3. Convert every individual order data folder in 'extracted' into a text, pass into object. Create new class readFromExtracted
#import jpg2data
#objectList = jpg2data.read2Data(extractedDirectory)
#for data in objectList:
    #data.getInfo()



#src/assets/extracted/21002546




