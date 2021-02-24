import os

directory = os.getcwd() + '/assets/convertedPDFs'
directoryList = os.listdir(directory)

if (directory + '.jpg') == ('/Users/andrewding/Desktop/ocrF21/src/assets/convertedPDFs' + '.jpg'):
    print("true")
else:
    print('false')

