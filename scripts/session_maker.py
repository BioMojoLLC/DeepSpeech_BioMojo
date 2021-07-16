# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 10:41:36 2021

Take in a long list of sentences

Take an id for a session to create 

generate a csv file with:
    
    Column1:  filename
    Column2:  filesize
    Column3:  transcript text

@author: rdhurlbu
"""
import numpy as np
import csv

# THIS MUST CHANGE EVERY TIME
# Each individual will get a unique session ID, this is that ID
session_id = 1002

# Number of sentences for the person to record
session_length = 30

# Base directory for creating sessions
dir_path = "D:/BioMojo/DeepSpeech/DataSets/Custom"

# Main pool of sentences to pull from 
input_file = dir_path + "/sentences.csv"

out_file = dir_path + f"/sessions/data-{session_id}.csv"

# Collect the sentences
with open(input_file, newline='') as csvfile:
    all_sentences = np.unique(list(csv.reader(csvfile)))

#%% Generate the data that goes into the table
session_transcripts = sorted(np.random.choice(all_sentences, session_length))
filenames = [f"{session_id}-{x}.wav" for x in range(session_length)]
filesizes = [''] * session_length

# Reformat the data as a list of tuples
rows = list(zip(filenames, filesizes, session_transcripts))

#%% Writing to csv file 
with open(out_file, 'w', newline='') as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile) 
        
    # writing the fields 
    csvwriter.writerow(['wav_filename',	'wav_filesize', 'transcript']) 
        
    # writing the data rows 
    csvwriter.writerows(rows)