import json
import pandas as pd
import bs4
import preprocessor as p
from gensim.parsing.preprocessing import remove_stopwords

def read_file(filename):
    '''
    Reads JSON file of tweets.

    Input: filename - name of file with tweets

    Output: tweets (list) - list of tweets, each tweet is a dictionary
    '''

    tweets = []
    for line in open(filename, 'r'):
        tweets.append(json.loads(line))

    return pd.DataFrame(tweets)

def process_row(row):
    
    text = row['text']
    text = text.lower()
    if text.find('vacc') > 0:
        text = p.clean(text)
        text = remove_stopwords(text)
        text_lxml = bs4.BeautifulSoup(text, "lxml")
        text_cln = text_lxml.get_text()
    else:
        text_cln = ''
    
    return text_cln

def pre_process_tweets(tweets):

    tweets['text_cln'] = tweets.apply(process_row, axis=1)
    tweets = tweets[tweets.text_cln != '']
    tweets['text_cln'] = tweets['text_cln'].str.replace('[^\w\s]',' ').str.replace('\s\s+', ' ')
    tweets.reset_index(drop=True)

    return tweets
            





