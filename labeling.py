import pandas as pd
import nltk
import numpy as np
import csv
from nltk.sentiment.vader import SentimentIntensityAnalyzer
# nltk.download('vader_lexicon') # need this if not yet downloaded

pd.set_option("display.max_colwidth", -1)
df = pd.read_csv('clean_tweet.csv',usecols=[1],names=['text'])[0:100]
df


def label(df):
    analyzer = SentimentIntensityAnalyzer()

    df['positive'] = df['text'].apply(lambda x:analyzer.polarity_scores(x)['pos'])
    df['neutral'] = df['text'].apply(lambda x:analyzer.polarity_scores(x)['neu'])
    df['negative'] = df['text'].apply(lambda x:analyzer.polarity_scores(x)['neg'])
    df['compound'] = df['text'].apply(lambda x:analyzer.polarity_scores(x)['compound'])
    return 


if __name__ == "__main__":
    label(df)
    