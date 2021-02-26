try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import cv2
import os, re


#specify path of tesseract bin cmd
pytesseract.pytesseract.tesseract_cmd = r'/usr/local/Cellar/tesseract/4.1.1/bin/tesseract'

styleText = pytesseract.image_to_string(Image.open('/Users/andrewding/Desktop/ocrF21/src/assets/extracted/20087677/style.jpg'))
trimmedStyle = styleText.strip()
#print(trimmedStyle)


poText = pytesseract.image_to_string(Image.open('/Users/andrewding/Desktop/ocrF21/src/assets/extracted/20087677/po.jpg'))
#trimmedPo = poText.strip()
poRegex = re.compile(r'\d\d\d\d\d\d\d\d')
poNumberAsList = poRegex.findall(poText)
#print(int(poNumberAsList[0]))

ihdText = pytesseract.image_to_string(Image.open('/Users/andrewding/Desktop/ocrF21/src/assets/extracted/20087677/ihd.jpg'))
ihdRegex = re.compile(r'\d\d/\d\d/\d\d\d\d')
ihdNumberAsList = ihdRegex.findall(ihdText)
#print(ihdNumberAsList[0])


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
    trimmedStyle = styleText.strip()
    return trimmedStyle

directory = '/Users/andrewding/Desktop/ocrF21/src/assets/extracted/20074433'
directoryList = os.listdir(directory)
ihdPath = os.path.join(directory, directoryList[1])
print(ihd_toString(ihdPath))
