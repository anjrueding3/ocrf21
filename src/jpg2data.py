try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import cv2
import os, re
from ExcelData import ExcelData


#specify path of tesseract bin cmd
pytesseract.pytesseract.tesseract_cmd = r'/usr/local/Cellar/tesseract/4.1.1/bin/tesseract'


#pass in ihd.jpg, return IHD
def ihd_toString(fileName):
    ihdText = pytesseract.image_to_string(Image.open(fileName))

    #use Regex with DD/DD/DDDD pattern
    ihdRegex = re.compile(r'\d\d/\d\d/\d\d\d\d')
    ihdNumberAsList = ihdRegex.findall(ihdText)
    return ihdNumberAsList[0]

#pass in po.jpg, return po number !!AS INTEGER!!
def po_toString(fileName):
    poText = pytesseract.image_to_string(Image.open(fileName))
    poRegex = re.compile(r'\d\d\d\d\d\d\d\d')
    poNumberAsList = poRegex.findall(poText)
    return(int(poNumberAsList[0]))

#pass in style.jpg, return Style,   !!!! REMEMBER TO USE EXCEPTION HANDLING. MIGHT THROW INDEX ERROR IF CAN"T BE MATCHED !!!!!!!
def style_toString(fileName):
    styleText = pytesseract.image_to_string(Image.open(fileName))
    #if it reads the STYLE#, replace it with blank, and trim it off so its all consistent
    if 'STYLE#' in styleText:
        styleText = styleText.replace('STYLE#', '')
    trimmedStyle = styleText.strip()
    return trimmedStyle


#should take extracted directory as parameter.
def read2Data(extractedDirectory):
    directoryList = os.listdir(extractedDirectory)
    #create objectList to store all extracted data objects
    objectList = []

    for folder in directoryList:
        fullPath = extractedDirectory  + '/' +  folder
        #for every directory in 'extracted', create a list to get ihd.jpg, po.jpg, and style.jpg. Try but throw exception if .DS_STORE pops up
        try:
            dataFolder = os.listdir(fullPath)
        except NotADirectoryError as error:
            print('NotADirectoryError exception: ' + folder + ' is not a directory.')

        #initialize data holders outside dataFile loop, to be added to objectList
        ihd = ''
        po = 0
        style = ''
        #append dataFile to full path to access file, run toString on each.
        for dataFile in dataFolder:
            fullFile = fullPath + '/' + dataFile

            try:
                if (dataFile.startswith('ihd')):
                    #print(ihd_toString(fullFile))
                    ihd = ihd_toString(fullFile)

                if (dataFile.startswith('po')):
                    #print(po_toString(fullFile))
                    po = po_toString(fullFile)

                if (dataFile.startswith('style')):
                    #print(style_toString(fullFile))
                    style = style_toString(fullFile)

            except NotADirectoryError as error:
                print('ERROR EXCEPTION(no worries though): NotADirectoryError: ' + fullPath + ' is not a directory')


        #for every folder, add extracted data to objectList as ExcelData object
        #skip if the fields aren't populated because of error thrown. This probably isn't the best way to do this but...
        if ihd != '':
            objectList.append(ExcelData(ihd, po, style))

    return objectList


    
#WATCH OUT FOR DS.STORE gotta figure out how to handle it.
