import pandas as pd
import nltk
import numpy as np
import csv
from glob import glob
import os
from nltk.sentiment.vader import SentimentIntensityAnalyzer
# nltk.download('vader_lexicon') # need this if not yet downloaded


def label(path, name, indicator):
    
    df = pd.read_csv(path + name + '.' + indicator)
    if 'score' in df.columns:
        print(name, ' is already processed.')
        return
    print(name, ', start processing')
    analyzer = SentimentIntensityAnalyzer()
   
    # df['positive'] = df['text_cln'].apply(lambda x:analyzer.polarity_scores(x)['pos'])
    # df['neutral'] = df['text_cln'].apply(lambda x:analyzer.polarity_scores(x)['neu'])
    # df['negative'] = df['text_cln'].apply(lambda x:analyzer.polarity_scores(x)['neg'])
    # df['compound'] = df['text_cln'].apply(lambda x:analyzer.polarity_scores(x)['compound'])

    df['positive'] = df['text'].apply(lambda x:analyzer.polarity_scores(x)['pos'])
    df['neutral'] = df['text'].apply(lambda x:analyzer.polarity_scores(x)['neu'])
    df['negative'] = df['text'].apply(lambda x:analyzer.polarity_scores(x)['neg'])
    df['compound'] = df['text'].apply(lambda x:analyzer.polarity_scores(x)['compound'])

    df['score'] = np.where(df['compound']>=0, 1, 0)

    print('---labeled!')
    print(df.head())

    df.to_csv(path +  name + '_labeled.json')
    return 


def main():
    path = os.getcwd()+'/Data/'
    for f in os.listdir(path):
        name, indicator = f.split('.')
        if indicator == 'csv':
            label(path, name, indicator)
    