#import pdf2jpg as convert
import extractPDF
import os

# 1. convert.directory_to_jpeg(/f21_pdfs)

# 2. now we have a convertedPDFS folder full of this runs pdfs

# 3. go through the list of files, extract ihd, po and style. How should i organize the extracted data?

# 4. Looks like i'm going to store each package of data in it's own directory within './assets/extracted'. Name directory filename + 'Data.

# 5. Need to remember to have an automated clear all assets, extracted, f21 pdfs, and converted pdfs function once i've confirmed everything is chillin.


#NOTES:
# Absolutely need my assets to look like this -->>  /Users/andrewding/Desktop/ocrF21/src/assets/extracted/21008188'
# Need to think of potential bugs




# 1. Pass in PDF Directory, convert to 'convertedPDFs' Folder
# convert.directory_to_jpeg('full path Name' + src/assets/f21_pdfs)


#2. directory to pass into extract_directory_data()
#imageFolder = os.getcwd() + '/src/assets/convertedPDFs'
#extractPDF.extract_directory_data(imageFolder)


#3. Convert every individual order data folder in 'extracted' into a text, pass into object




#src/assets/extracted/21002546




