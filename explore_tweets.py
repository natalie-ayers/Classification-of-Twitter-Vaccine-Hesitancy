"""
Code taken from/inspired by:
https://github.com/thepanacealab/covid19_twitter/blob/master/COVID_19_dataset_Tutorial.ipynb
"""

import random 
import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt


no_samples = "1000" #@param {type:"string"}
list_tweets = None

with open("hydrated_tweets_short.json", "r") as myfile:
    list_tweets = list(myfile)

if int(no_samples) > len(list_tweets):
    no_samples = len(list_tweets)

sample = random.sample(list_tweets, int(no_samples))

file = open("sample_data.json", "w")
for i in sample:
  file.write(i)
file.close() #This close() is important

!python parse_json_lite.py sample_data.json p


FILLER_WORDS = ["", "the", "to", "of", "in", "is", "and", "a", "for", "on", \
        "be", "as", "are", "have", "this", "the", "has", "from", "at", "that", \
        "-", "&amp;", "by", "|", "it", "was", "an"]

no_top_unique_words = "30" #@param {type:"string"}

df = pd.read_csv('sample_data.tsv',sep="\t")

result = Counter(" ".join(df['text'].values.tolist()).split(" ")).items()
df2 = pd.DataFrame(result)
df2.columns =['Word', 'Frequency']
df2.Word = df2.Word.str.lower()
df2 = df2[~df2.Word.isin(FILLER_WORDS)] #Deletes the empty spaces counted
df2 = df2.sort_values(['Frequency'], ascending=[False]) #Sort dataframe by frequency (Descending)

print('\033[1mTop '+no_top_unique_words+' most unique words used from the dataset\033[0m \n')
print(df2.head(int(no_top_unique_words)).to_string(index=False)) #Prints the top N unique words used
print("\n")
df3 = df2.head(int(no_top_unique_words))
df3.plot(y='Frequency', kind='pie', labels=df3['Word'], figsize=(9, 9), autopct='%1.1f%%', title='Top '+no_top_unique_words+' most unique words used from the dataset')