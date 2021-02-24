import os

filename = '/Users/andrewding/Desktop/ocrF21/assets/f21_pdfs/21002046.pdf'
directory = os.getcwd() + '/assets/convertedPDFs'
directoryList = os.listdir(directory)

print(directoryList)
