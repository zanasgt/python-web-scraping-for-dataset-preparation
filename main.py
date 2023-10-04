# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 16:40:47 2023

@author: PC
"""

import collect_articles
import pdf2txt
import os


rootdir = os.path.dirname(__file__)

#branches = ["Çocuk+Sağlığı+ve+Hastalıkları+Anabilim+Dalı"]

branches = ["Acil+Tıp+Anabilim+Dalı", 
            "Çocuk+Sağlığı+ve+Hastalıkları+Anabilim+Dalı",
            "Deri+ve+Zührevi+Hastalıkları+Anabilim+Dalı", 
            "Enfeksiyon+Hastalıkları+ve+Klinik+Mikrobiyoloji+Anabilim+Dalı",
            "Fiziksel+Tıp+ve+Rehabilitasyon+Anabilim+Dalı", 
            "Göğüs+Hastalıkları+Anabilim+Dalı",
            "Halk+Sağlığı+Anabilim+Dalı", 
            "İç+Hastalıkları+Anabilim+Dalı", 
            "Kardiyoloji+Anabilim+Dalı",
            "Nöroloji+Anabilim+Dalı", 
            "Ruh+Sağlığı+ve+Hastalıkları+Anabilim+Dalı", 
            "Tıbbi+Genetik+Anabilim+Dalı"]


try:
    collect_articles.download_department_articles(branches)
except:
    print("An error occured while downloading articles.")
    

pdf_list = pdf2txt.search_pdf('.pdf', rootdir)
pdf2txt.convert_pdf_to_txt(pdf_list)