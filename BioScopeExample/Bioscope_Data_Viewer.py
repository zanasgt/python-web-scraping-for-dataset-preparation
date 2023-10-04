# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 20:36:23 2023

@author: PC
"""

import pandas as pd
import re
from googletrans import Translator
#import deepl pro account needed

df = pd.read_csv(r'"D:\Thesis\DataSets\Connen Doyle\SEM-2012-SharedTask-CD-SCO-training-09032012.xlsx"')
df_filtered = df.query("target == 1")
df_filtered = df_filtered.reset_index()
df_filtered = df_filtered.drop(columns=['sentence_id', 'target', 'index'])
'''df_filtered['cue1'] = ''
df_filtered['scope1'] = ''
df_filtered['cue2'] = ''
df_filtered['turkce'] = None'''

df_filtered = df_filtered.assign(cue1='', scope1='', cue2='', turkce = '')

df_dict = df_filtered.to_dict('records')
for idx in df_filtered.index:
#for idx, cue_span in df_filtered['cue_span'].iteritems():
    sentence = df_filtered['sentence'][idx]
    scope_span = df_filtered['scope_span'][idx]
    cue_span = df_filtered['cue_span'][idx]
    a = re.findall(r'[\d]+', scope_span)
    scope_begin = int(a[0])
    scope_end = int(a[1])
    scope = sentence[scope_begin:scope_end]
    df_filtered['scope1'][idx] = scope
    b = re.findall(r'[\d]+', cue_span)
    cue_begin = int(b[0])
    cue_end = int(b[1])
    cue = sentence[cue_begin:cue_end]
    df_filtered['cue1'][idx] = cue
    if len(b) >3:
        cue_begin = int(b[2])
        cue_end = int(b[3])
        cue = sentence[cue_begin:cue_end]
        df_filtered['cue2'][idx] = cue
    translator = Translator()
    result = translator.translate(sentence, src='en', dest='tr')
    df_filtered['turkce'][idx] = result.text
    #translator = deepl.Translator('zana.1989')
    #result = translator.translate_text(sentence, target_lang="TR")
    #df_filtered['turkce'][idx] = result.text

df_filtered = df_filtered.drop(columns=['cue_span', 'scope_span'])
df_filtered = df_filtered.sort_values('cue1')   
#translator = Translator()
#df_filtered['Turkce'] = df['value'].apply(translator.translate, src='es', dest='en').apply(getattr, args=('text',))     
# determining the name of the file
file_name = 'BioScope.xlsx'
  
# saving the excel
df_filtered.to_excel(file_name)