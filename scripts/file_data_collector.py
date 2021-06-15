# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 17:31:39 2021


This is just a helper script to collect hundreds of file names 
and their associated sizes to spit into a csv file together


@author: rdhurlbu
"""

import os
import pandas as pd
import numpy as np


dir_name = 'D:/Biomojo/DeepSpeech/data_new/data'

# Collect a list of file names
files = list( filter( lambda x: os.path.isfile(os.path.join(dir_name, x)),
                        os.listdir(dir_name) ) )

# Collect a list of sizes for each file
sizes = [os.stat(os.path.join(dir_name, file_name)).st_size  
                    for file_name in files ]

# Construct a simple df 
df = pd.DataFrame({"wav_filesize": sizes})

# DataFrame index is filenames
df.index = files
df.index.name = "wav_filename"

# There is an empty series in the Dataframe
# TODO add a way to collect this information and store it here
df['transcript'] = np.NAN
df.to_csv("bm_new.csv")
