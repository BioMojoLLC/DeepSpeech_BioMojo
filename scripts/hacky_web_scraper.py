# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 09:07:23 2021

@author: Ryan Hurlbut
"""
import re

source = 'triage-related'
key_words = [' IV ', ' IO ', 'lock', 'nasopharyngeal', 'HPMK', 'hypothermia', 'intubation', 'intubate' ]

raw_text_file = f'raw-{source}.txt'

# import text file
with open(raw_text_file, newline='\n',errors='ignore') as file:
  lines = file.readlines()

# Convert list to string
raw_txt = ''
for line in lines:
    raw_txt = raw_txt+line
raw_txt = re.sub('[\r\n[\]\(\)]','', raw_txt).lower()

# Split by line 
raw_sentences = re.split('[.?!:]', raw_txt)

# Filter out lines by key word
def filter_by_kwords(kwords : list, sentence : str) -> bool:
    for word in kwords:
        if word in sentence:
            return True
    return False

filtered_sentences = list( filter( lambda x: filter_by_kwords(key_words, x), raw_sentences))

filtered_sentences = [line.strip( ', ') + '\n' for line in filtered_sentences]


print("Found", len(filtered_sentences), "sentences with key words in" , raw_text_file)
# save to file
out_file = f'cleaned-{source}-test.txt'
print("Saving to", out_file)
with open(out_file, 'w', newline='\n') as file:
    file.writelines(filtered_sentences)