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

#function called by clear button
def clearFolders():

    pdfFolder = os.getcwd() + '/assets/f21_pdfs'
    pdfList = os.listdir(pdfFolder)
    for files in pdfList:
        if files.endswith('pdf'):
            print(os.path.join(pdfFolder, files))

    convertedFolder = os.getcwd() + '/assets/convertedPDFs'
    convertedList = os.listdir(convertedFolder)
    for files in convertedList:
        if files.endswith('jpg'):
            print(os.path.join(convertedFolder, files))

    extractedFolder = os.getcwd() + '/assets/extracted'
    extractedList = os.listdir(extractedFolder)
    for files in extractedList:
        print(os.path.join(extractedFolder, files))

    

    


#executes entire program when button clicked
#need to make sure it doesn't mess up somehow, like if the pathname doesn't exist. 
# needs to inform user that the process has been completed
def getStuff():

    #if this directory isn't empty, notify. This DS.store is mesesing with me again. 
    if os.listdir(os.getcwd() + '/assets/convertedPDFs') != 0:
        clearFolderPopup()
    else:
        sourcePDF = pdfPathBox.get()
        targetExcel = excelBox.get()
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
