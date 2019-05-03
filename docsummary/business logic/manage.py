import variables
variables.initialize()
import pdf2txt
import extractor
import pdf_downloader
#from pdf_downloader import download_count
import os
import argparse

parser = argparse.ArgumentParser(description='Description of your program')
parser.add_argument('-a','--add', help='Add a pdf file to convert to text', required=True)
args = vars(parser.parse_args())

if args['add']:
    documentName = args['add']

os.system('python pdf2txt.py ' + documentName)

#extractor.extrac()
#pdf_downloader.download()


        
                
   
