import pdf2image
from pdf2image import convert_from_path
import os



#images = convert_from_path('/Users/andrewding/Desktop/ocrF21/assets/f21_pdfs/20087677.pdf', dpi = 300, fmt = "jpeg", first_page= 1, single_file=True, output_folder= "/Users/andrewding/Desktop/ocrF21/assets/convertedPDFs", output_file= fileName)


def pdf2jpeg(filePath):
    
    #extract string between last / and .pdf to use as output file name
    outputName = filePath[filePath.rfind('/') + 1 : filePath.rfind('.pdf')] 
    outputDirectory =  os.getcwd() + '/assets/convertedPDFs'


    #convert pdf to jpg, output to location in assets folder, output as outputName + .jpg
    images = convert_from_path(filePath, dpi = 300, fmt = "jpeg", first_page= 1, single_file=True, output_folder= "/Users/andrewding/Desktop/ocrF21/src/assets/convertedPDFs", output_file= outputName)


directory = '/Users/andrewding/Desktop/ocrF21/src/assets/f21_pdfs'


#list all files in pdf directory, convert them to jpg if they end with '.pdf'
def directory_to_jpeg(directory):
    directoryList = os.listdir(directory)
    for file in directoryList:
        if file.endswith('.pdf'):
            pdf2jpeg(os.path.join(directory, file))    #run pdf2jpeg on full path of each file in directory

directory_to_jpeg(directory)