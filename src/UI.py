import tkinter as tk
from tkinter import *
import pdf2jpg as convert
import extractPDF
import jpg2data
import updateExcel
import os, sys



#temporarily run from UI.py as main while i figure this ish out
    
window = tk.Tk()
window.title('GUI')
window.geometry('500x500')


def getStuff():
    sourcePDF = pdfPathBox.get()
    targetExcel = excelBox.get()
    convertedImageFolder = os.getcwd() + '/assets/convertedPDFs'
    extractedFolders = os.getcwd() + '/assets/extracted'
    convert.directory_to_jpeg(sourcePDF)
    extractPDF.extract_directory_data(convertedImageFolder)
    objectList = jpg2data.read2Data(extractedFolders)
    updateExcel.updateExcel(objectList, targetExcel)

    #convert.directory_to_jpeg(sourcePDF)
    


#build source
pdf_folder_label = tk.Label(text = "Paste PDF folder path below:")
pdf_folder_label.grid(column = 0, row = 0, padx = 150, pady = (20,0))

pdfPathBox = Entry(window, width = 30)
pdfPathBox.grid(row = 1, column  = 0, pady = (0,50))

targetExcelLabel = tk.Label(text = "Paste Target Excel Path below:")
targetExcelLabel.grid(column = 0, row = 2)

excelBox = Entry(window, width = 30)
excelBox.grid(row = 3, column = 0)

myButton = tk.Button(window, text = 'Enter', command = getStuff)
myButton.grid(row = 4, column = 0, sticky = tk.W, pady = 5)


window.mainloop()