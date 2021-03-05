import tkinter as tk
from tkinter import *
import pdf2jpg as convert
import extractPDF
import jpg2data
import updateExcel
import os, sys


#TOdo:
#1. Create clear method to run when 'clear' button is pressed.
    # - Make sure you don't delete all your files like a dumbo
    # - Check each asset folder, li


#temporarily run from UI.py as main while i figure this ish out
    
window = tk.Tk()
window.title('GUI')
window.geometry('500x500')



#confirmation popup
def confirmationWindow():
    #creates new window using Toplevel
    confirmPopup = Toplevel(window)
    confirmPopup.title('Confirmation')
    confirmPopup.geometry("500x300")
    tk.Label(confirmPopup, text = 'Finished Running').pack(padx = 30, pady = 30)

#inform user to clear folders
def clearFolderPopup():
    clearPopup = Toplevel(window)
    clearPopup.title('CLEAR FOLDERS (PRESS CLEAR BUTTON)')
    clearPopup.geometry("500x500")
    tk.Label(clearPopup, text = "MUST CLEAR FOLDERS BEFORE PROCEEDING!!").pack(padx = 50, pady = 200)


############################### !!!!!!!!!!!  SENSITIVE CODE. BE CAREFUL DONT DELETE ALL YOUR FILES  !!!!!!!! ##################################

#function called by clear button
def clearFolders():

    #specify pdfs folder path in assets, list all files so i can loop through and delete them
    pdfFolder = os.getcwd() + '/assets/f21_pdfs'
    pdfList = os.listdir(pdfFolder)
    for files in pdfList:
        #if they end with pdf or are DS.Store, then delete them
        if files.endswith('pdf') or files.endswith('Store'):
            os.remove(os.path.join(pdfFolder, files))
            print('REMOVING '  + os.path.join(pdfFolder,files))
    #log to console
    if len(os.listdir(pdfFolder)) == 0:
        print(pdfFolder + ' is clear!\n\n')

    #specify convertedPDFS path, list all files, loop through and delete.
    convertedFolder = os.getcwd() + '/assets/convertedPDFs'
    convertedList = os.listdir(convertedFolder)
    for files in convertedList:
        #if files are jpg or DS.Store, then delete
        if files.endswith('jpg') or files.endswith('Store'):
            os.remove(os.path.join(convertedFolder, files))
            print('REMOVING ' + os.path.join(convertedFolder, files))
    #log to console
    if len(os.listdir(convertedFolder)) == 0:
        print(convertedFolder + ' is clear!\n\n')

    extractedFolder = os.getcwd() + '/assets/extracted'
    extractedList = os.listdir(extractedFolder)
    #for files within extracted, if it ends with Store, remove it, if its a directory, empty it's contents, then delete it
    for files in extractedList:
        if files.endswith('Store'):
            os.remove(os.path.join(extractedFolder, files))
            print('REMOVING ' + os.path.join(extractedFolder, files))
        else:
            #inner directory is full path + direcotry name(aka files)
            innerDirectory = os.path.join(extractedFolder, files)
            fileList = os.listdir(innerDirectory)
            #for jpg files in each inner directory. Remove it so we can delete the directory
            for jpg in fileList:
                os.remove(os.path.join(innerDirectory, jpg))
                print('REMOVING ' + os.path.join(innerDirectory, jpg))

        os.rmdir(os.path.join(extractedFolder, files))
        print('REMOVING DIRECTORY ' + os.path.join(extractedFolder, files))

    if len(os.listdir(extractedFolder)) == 0:
        print(extractedFolder + ' is clear!\n\n')
            
        

################################# !!!!!!!!!!!  SENSITIVE CODE. BE CAREFUL DON"T DELETE ALL YOUR FILES PLEASEEE  !!!!!!!! ###################################



#executes entire program when button clicked
#need to make sure it doesn't mess up somehow, like if the pathname doesn't exist. 
# needs to inform user that the process has been completed
def getStuff():

    #if this directory isn't empty, notify. This DS.store is mesesing with me again. 
    if len(os.listdir(os.getcwd() + '/assets/convertedPDFs')) != 0:
        clearFolderPopup()

    #if it is empty, then run the data extraction methods. THIS IS PRETTY MUCH THE NEW MAIN LOGIC
    else:
        sourcePDF = pdfPathBox.get()
        targetExcel = excelBox.get()

        #add if logic, to check if sourcePDF path ends with 'pdfs', or if targetExcel ends with '.xlsx' to confirm the correct path.

        convertedImageFolder = os.getcwd() + '/assets/convertedPDFs'
        extractedFolders = os.getcwd() + '/assets/extracted'
        convert.directory_to_jpeg(sourcePDF)
        extractPDF.extract_directory_data(convertedImageFolder)
        objectList = jpg2data.read2Data(extractedFolders)
        updateExcel.updateExcel(objectList, targetExcel)
        confirmationWindow()
    
#/Users/andrewding/Desktop/ocrF21/src/assets/f21_pdfs
#/Users/andrewding/Desktop/targetExcel.xlsx

#build source
pdf_folder_label = tk.Label(text = "Paste PDF folder path below:")
pdf_folder_label.grid(column = 0, row = 0, padx = 150, pady = (20,0))

pdfPathBox = Entry(window, width = 30)
pdfPathBox.grid(row = 1, column  = 0, pady = (0,50))

targetExcelLabel = tk.Label(text = "Paste Target Excel Path below:")
targetExcelLabel.grid(column = 0, row = 2)

excelBox = Entry(window, width = 30)
excelBox.grid(row = 3, column = 0)

#create enter button, calls getStuff() when clicked
myButton = tk.Button(window, text = 'Enter', command = getStuff)
myButton.grid(row = 4, column = 0, sticky = tk.W, pady = 25, padx = 245)

clearLabel = tk.Label(text = "CLICK CLEAR TO EMPTY FOLDERS")
clearLabel.grid(row = 5, column = 0, pady = (75, 0))

#create clear button, calls deleteFolders() when clicked
clearButton = tk.Button(window, text = 'Clear', command = clearFolders)
clearButton.grid(row = 6, column = 0, sticky = tk.E, pady = 25, padx = 245)


window.mainloop()
