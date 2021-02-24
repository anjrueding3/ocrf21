import pdf2image
from pdf2image import convert_from_path
import os


#take in file path name, convert to pdf to output directory within project folder, don't need to check for redudancy, if it exists it will be overwritten
def pdf2jpeg(filePath):
    
    #extract string between last / and .pdf to use as output file name
    outputName = filePath[filePath.rfind('/') + 1 : filePath.rfind('.pdf')] 
    outputDirectory =  os.getcwd() + '/assets/convertedPDFs'
   
    #convert pdf to jpg, output to location in assets folder, output as outputName + .jpg
    images = convert_from_path(filePath, dpi = 300, fmt = "jpeg", first_page= 1, single_file=True, output_folder= outputDirectory, output_file= outputName)



#list all files in pdf directory, convert them to jpg if they end with '.pdf'
def directory_to_jpeg(directory):
    directoryList = os.listdir(directory)
    for file in directoryList:
        if file.endswith('.pdf'):
            pdf2jpeg(os.path.join(directory, file))    #run pdf2jpeg on full path of each file in directory


directory = os.getcwd() + '/assets/f21_pdfs'
directory_to_jpeg(directory)