# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 15:17:20 2023

@author: PC
"""

# for colab you can pip install, for anaconda you can install library
# on your environment

import PyPDF2
import os

rootdir = r'C:\Users\PC\Desktop\Negation Corpus\AcilTıpAnabilimDalı' #'path/to/dir'
pdf_list = []

def search_pdf(extension, rootdir):
    for (dirpath, dirnames, filenames) in os.walk(rootdir):
        for filename in filenames:
            if os.path.splitext(filename)[-1] == extension:
                pdf_list.append(os.path.join(dirpath, filename))

def convert_pdf_to_txt(pdf_list):
    '''
    Take a pdf directroy list, convert and save them as txt
    '''
    for pdf_path in pdf_list:
        texts=[]
        text = ''
        #Creating pdf object by reading file
        pdf = open(pdf_path, 'rb')
        #Create PyPDF2 object
        pdfReader = PyPDF2.PdfFileReader(pdf, strict=False)
        #info = pdfReader.getDocumentInfo()
        number_of_pages = len(pdfReader.pages)
        #i = info.creator()
        i = 0
        for i in range(number_of_pages):
            page = pdfReader.getPage(i)
            a = page.get_contents()
            text += page.extractText()
        text = text.replace('\n', '')
        text = text.replace('.', '.\n')
           
        text_path = pdf_path.replace('.pdf', '')
        with open(text_path+'.txt', 'w', encoding="utf-16") as f:
            f.write(text)
        print('%')


search_pdf('.pdf', rootdir)
convert_pdf_to_txt(pdf_list)