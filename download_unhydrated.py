"""
Modifying to hydrate COVID tweets from tutorial at:
https://github.com/thepanacealab/covid19_twitter/blob/master/COVID_19_dataset_Tutorial.ipynb

"""

import sys
import gzip
import shutil
import os
import wget
import csv
import linecache
from shutil import copyfile
import ipywidgets as widgets
import numpy as np
import pandas as pd

import json
import tweepy
from tweepy import OAuthHandler

#daily_dt = '2021-04-14'
daily_dt = sys.argv[1]
dataset_URL = ("https://github.com/thepanacealab/covid19_twitter/raw/master/dailies/" + 
                daily_dt + '/' +
                daily_dt + "_clean-dataset.tsv.gz") 

print('Downloading gzip file ',daily_dt,' from dailies..')
print('')

#Downloads the dataset (compressed in a GZ format)
out_file_gz = 'data/' + daily_dt + '_clean-dataset.tsv.gz'
in_file = 'data/' + daily_dt + '_clean-dataset.tsv'

wget.download(dataset_URL, out=out_file_gz)

print('Unzipping gzip file..')
print('')

#Unzips the dataset and gets the TSV dataset
with gzip.open(out_file_gz, 'rb') as f_in:
    with open(in_file, 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)

#Deletes the compressed GZ file
os.unlink(out_file_gz)


# Could also filter by country, but very sparsely populated
# Eg, from a subset of data from a single day, had:
  # country_code  nunique of tweet_id
  # NaN 170537
  # US  1202
  # IN  837
  # CA  468
  # GB  342
  # ....

print('Creating English-only filtered dataset')
print('')
clean_filt = 'data/' + daily_dt + '_clean-dataset-filtered.tsv'

#Creates a new clean dataset with the specified language (if specified)
filtered_language = 'en'

#If no language specified, it will get all records from the dataset
if filtered_language == "":
  copyfile(in_file, clean_filt)

#If language specified, it will create another tsv file with the filtered records
else:
  filtered_tw = list()
  current_line = 1
  with open(in_file) as tsvfile:
    tsvreader = csv.reader(tsvfile, delimiter="\t")

    if current_line == 1:
      filtered_tw.append(linecache.getline(in_file, current_line))

      for line in tsvreader:
        if line[3] == filtered_language:
          filtered_tw.append(linecache.getline(in_file, current_line))
        current_line += 1

  print('\033[1mShowing first 5 tweets from the filtered dataset\033[0m')
  print(filtered_tw[1:(6 if len(filtered_tw) > 6 else len(filtered_tw))])

  with open(clean_filt, 'w') as f_output:
      for item in filtered_tw:
          f_output.write(item)

print('Wrote filtered ',daily_dt,' unhydrated tweets to ',clean_filt)
print('')




