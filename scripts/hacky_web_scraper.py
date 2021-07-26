# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 09:07:23 2021

Script for collecting and saving text related to key words. 

PARAMETERS:
    source: 
        This is the general subject matter. Your input file for this script 
        needs to be named in the format "raw-{source}". Where source is the 
        general subject matter the vocabulary words surround. 
            
    key_words: 
        This is a list of words to select upon. Sentences will be saved and
        if entered on it's own line if they contain at east one word in this 
        list. 

RETURNS:
    The output file of the program will save to "cleaned-{source}.txt".


Usage:
    The most simple usage of this script is to perform the following steps:
        1. Find a web page you want to scrape from. 
        2. Ctrl + A , Ctrl + C (CMD for mac). 
        3. Paste text into a basic text file
        4. Repeat for as many web pages as you wish
        5. Save file as "raw-{source}.txt" where source is your general subject matter
        6. Open up the script, change the source variable to the source saved in the 
            above file name.
        7. In the key_words variable, enter the key words you want to select sentences with
        8. Run. 
        9. Check the outut file, remove any irrelevant or useless lines. (There will be a few)

@author: Ryan Hurlbut
"""
import re

# CHANGE ME
source = 'medical'
key_words = ['medical', 'or', 'other', 'interesting', 'words' ]

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