try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import cv2
import os

#specify path of tesseract bin cmd
pytesseract.pytesseract.tesseract_cmd = r'/usr/local/Cellar/tesseract/4.1.1/bin/tesseract'


#call in loop to create directories that will organize extracted data
def create_data_directories(groupedDataDirectory, fileName):
    miniDataDirectories = (groupedDataDirectory + '/' + fileName[:-4])
    try:
        os.mkdir(miniDataDirectories)
    except OSError as error:
        print(error)


#crop IHD box from jpg, save as new jpg called ihd.jpg
def cropIHD(sourceImage, outputFolder):
    imgPath = sourceImage
    outputFilePath = outputFolder + '/ihd.jpg'
    img = cv2.imread(imgPath)
    ihdTag = img[638:750, 1175:1438]
    cv2.imwrite(outputFilePath, ihdTag)

#crop PO box from jpg, save as new jpg called po.jpg
def cropPO(sourceImage, outputFolder):
    imgPath = sourceImage
    outputFilePath = outputFolder + '/po.jpg'
    img = cv2.imread(imgPath)
    poTag = img[1255:1385, 145:350]
    cv2.imwrite(outputFilePath, poTag)

#crop Style box from jpg, save as new jpg called style.jpg in respective folder
def cropStyle(sourceImage, outputFolder):
    imgPath = sourceImage
    outputFilePath = outputFolder + '/style.jpg'
    img = cv2.imread(imgPath)
    styleTag = img[1255:1385, 350:605]
    cv2.imwrite(outputFilePath, styleTag)
    
    
  
#pass in converted PO jpg directory, create directory from each file, extract necessary data and store in directory packages
def extract_directory_data(directory):

    #create list of all file Names in directory
    directoryList = os.listdir(directory)

    #create full path to extracted data folder in 'assets'. Going to append the new organized data folders to this in the loop
    groupedDataDirectoryPath = directory[:directory.rfind('/')] + '/extracted'

    #create a directory to store associated data for each PO order
    for file in directoryList:
        create_data_directories(groupedDataDirectoryPath, file)
    
    #now for every order/jpg, search the extracted folder for the matching one, and populate it and break if it matches
    for file in directoryList:
        searchName = file[:-4]
        extractedList = os.listdir(groupedDataDirectoryPath)
        for folderName in extractedList:
            if folderName == searchName:
                targetFolder = groupedDataDirectoryPath + '/' + searchName
                sourceImage = directory + '/' + file
                #run extract functions, specify source image and target Output folder as parameters
                #runExtractPO()
                #run ExtractIHD()
                #run ExtractStyle()
                cropIHD(sourceImage, targetFolder)
                cropPO(sourceImage, targetFolder)
                cropStyle(sourceImage, targetFolder)
                break
            



