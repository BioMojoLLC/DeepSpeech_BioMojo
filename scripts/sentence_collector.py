# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 15:16:10 2021

Script for cutting out sentences with key words from large text files and 
saving the sentences to a new file. 

@author: rdhurlbu
"""
import re
from string import digits


# Location of the file you would like to read
in_file = 'D:/BioMojo/DeepSpeech/DataSets/TextOnly/train.txt'

# File to append sentences to
out_file = 'D:/BioMojo/DeepSpeech/DataSets/TextOnly/out.txt'

# Word we want to strip sentences for
key_word = ' ibs '

# Read in file, strip sentences, write them to the new file. 
with open(in_file, 'r') as file :
    raw_txt = file.read().lower()
    raw_txt = re.sub(r'[^a-z .\d]+', '', raw_txt)
    cleaned_sentences = [s + '.\n' for s in raw_txt.split('.') if key_word in s]
    print(f"Read {len(cleaned_sentences)} sentences with {key_word} from {in_file}")
    cleaned_sentences = ''.join(cleaned_sentences)
    cleaned_sentences = cleaned_sentences.replace(".", "")

with open(out_file, 'a') as file:
    file.write(cleaned_sentences)    
