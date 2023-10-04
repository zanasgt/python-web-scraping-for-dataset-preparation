# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 15:17:20 2023

@author: PC
"""

# for colab you can pip install, for anaconda you can install library
# on your environment

import PyPDF2
import os
from pathlib import Path
import re

pdf_list = []

'''
This function is search for directories, visit them and take pdf files
into a list to process.
Please aware that we are not filtering the files to search pdf.
This is an exhaustive search and this is OK for this code because 
there are not much file not including pdf and other files not including pdf
'''
def search_pdf(extension, rootdir):
    for (dirpath, dirnames, filenames) in os.walk(rootdir):
        for filename in filenames:
            if os.path.splitext(filename)[-1] == extension:
                pdf_list.append(os.path.join(dirpath, filename))
    return pdf_list

"""
Please aware that this function not 100% make clear as it will still
need handcraft correction for negative numbers for - replacement and so on..
But it will generally ease my work due to my dataset.
You need to monitor some of your dataset text and decide which format of 
replacement or correction will more ease your work for later process.
"""

def clean_text(input_text):

    # Add a newline after each "."
    cleaned_text = re.sub(r'\.(?![0-9])\s*', '.\n', input_text)
    
    # Remove beginning and ending spaces and tabs
    cleaned_text = cleaned_text.strip()

    # Replace multiple spaces with a single space
    cleaned_text = re.sub(' +', ' ', cleaned_text)

    # Replace " '" with "'"
    cleaned_text = cleaned_text.replace(" '", "'").replace("' ", "'")

    # Replace " -", " - ", and "- " with "-"
    cleaned_text = re.sub(r'\s*-\s*', '-', cleaned_text)
    
    # Replace "( ", " )" with "(" and ")"
    cleaned_text = cleaned_text.replace("( ", "(").replace(" )", ")")
    
    # Replace special characters
    cleaned_text = cleaned_text.replace('\udb40', 'BBBBBUUUU')
    
    # Correct Turkish special words for ease of use
    cleaned_text = cleaned_text.replace(' ya da ', ' yada ')
    cleaned_text = cleaned_text.replace(' ve ya ', ' veya ')

    return cleaned_text

def convert_pdf_to_txt(pdf_list):
    '''
    Take a pdf directroy list, convert and save them as txt
    '''
    for pdf_path in pdf_list:
        text = ''
        #Creating pdf object by reading file
        with open(pdf_path, 'rb') as pdf:
            #Create PyPDF2 object
            pdfReader = PyPDF2.PdfReader(pdf, strict=False)
            #info = pdfReader.getDocumentInfo()
            number_of_pages = len(pdfReader.pages)
            #i = info.creator()
            i = 0
            for i in range(number_of_pages):
                page = pdfReader.pages[i]
                # content = page.get_contents()
                text += page.extract_text()
                text = clean_text(text)
                
            text_path = pdf_path.replace('.pdf', '.txt')
            text_name = Path(text_path).name
        
        
        with open(text_path, 'w', encoding="utf-16") as f:
            f.write(text)
        print(f"{text_name} has been written..\n")