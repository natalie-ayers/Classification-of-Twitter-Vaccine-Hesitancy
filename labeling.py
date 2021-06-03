import pandas as pd
import nltk
import numpy as np
import csv
from glob import glob
import os.path
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import re
# nltk.download('vader_lexicon') # need this if not yet downloaded


def label(path, name, indicator):
    '''
    new_words = {
    'foo': 2.0,
    'bar': -3.4,
}

SIA = SentimentIntensityAnalyzer()

SIA.lexicon.update(new_words)
    '''
    try:
        df = pd.read_csv(path + name + '.' + indicator)
    except:
        # when the file cannot be read, force using line terminator n, not r:
        df = pd.read_csv(path + name + '.' + indicator, lineterminator='\n')
        df['text_cln_tok'] = df['text_cln_tok'].apply(lambda x: re.sub("\r",'', x))

    if 'score' in df.columns:
        print(name, ' is already processed.')
        return
  
    print(name, ', start processing')
    analyzer = SentimentIntensityAnalyzer()


    # Cleaning, remove na, remove unnecessary special characters
    df = df[df['text_cln_tok'].notna()]
    df['tmp'] = df['text_cln_tok'].apply(lambda x: re.sub("',",'', x))
    df['tmp'] = df['tmp'].apply(lambda x: re.sub("'",'', x))

    #print(df['text_cln_tok'].head())
    
    # Labeling
    df['positive'] = df['tmp'].apply(lambda x:analyzer.polarity_scores(x)['pos'])
    df['neutral'] =  df['tmp'].apply(lambda x:analyzer.polarity_scores(x)['neu'])
    df['negative'] = df['tmp'].apply(lambda x:analyzer.polarity_scores(x)['neg'])
    df['compound'] = df['tmp'].apply(lambda x:analyzer.polarity_scores(x)['compound'])
    
    df['score'] = np.where(df['compound']>=0.05, 1, (np.where(df['compound']> -0.05,0,-1)))

    print(df['compound'].head())
    print('---labeled!')

    # Save file to json
    if not os.path.isdir(os.path.join(path,"labeled")):
        os.mkdir(os.path.join(path,"labeled"))

    df[['created_at','text_cln','text_cln_tok', 'positive', 'neutral', 'negative', 'compound',
       'score']].to_json(os.path.join(path,"labeled/") + name + '_labeled.json')
    return 
 

def main():
    path = os.getcwd()+'/Data/'
    for f in os.listdir(path):
        if len(f.split('.'))!=2:
            continue
        name, indicator = f.split('.')
        if os.path.isfile(path + '/labeled/' +name+'_labeled.json'):
            continue
        elif indicator == 'csv':
            try:
                label(path, name, indicator)
                os.unlink(os.path.join(path, f))
            except Exception as e: 
                print(e)
                print(name +' could not be processed. skip')
    