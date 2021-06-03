import json
import pandas as pd
import pre_process
import seaborn as sns

def pull_num_rec():

    files = [
"2021-01-01_hydrated_tweets_short.json",
"2021-01-05_hydrated_tweets_short.json",
"2021-01-09_hydrated_tweets_short.json",
"2021-01-13_hydrated_tweets_short.json",
"2021-01-17_hydrated_tweets_short.json",
"2021-01-21_hydrated_tweets_short.json",
"2021-01-25_hydrated_tweets_short.json",
"2021-01-29_hydrated_tweets_short.json",
"2021-02-02_hydrated_tweets_short.json",
"2021-02-06_hydrated_tweets_short.json",
"2021-02-10_hydrated_tweets_short.json",
"2021-02-14_hydrated_tweets_short.json",
"2021-02-18_hydrated_tweets_short.json",
"2021-02-22_hydrated_tweets_short.json",
"2021-02-26_hydrated_tweets_short.json",
"2021-03-02_hydrated_tweets_short.json",
"2021-03-06_hydrated_tweets_short.json",
"2021-03-10_hydrated_tweets_short.json",
"2021-03-14_hydrated_tweets_short.json",
"2021-03-18_hydrated_tweets_short.json",
"2021-03-22_hydrated_tweets_short.json",
"2021-03-26_hydrated_tweets_short.json",
"2021-03-30_hydrated_tweets_short.json",
"2021-04-03_hydrated_tweets_short.json",
"2021-04-07_hydrated_tweets_short.json",
"2021-04-11_hydrated_tweets_short.json",
"2021-04-15_hydrated_tweets_short.json",
"2021-04-19_hydrated_tweets_short.json",
"2021-04-23_hydrated_tweets_short.json",
"2021-04-27_hydrated_tweets_short.json",
"2021-05-01_hydrated_tweets_short.json",
"2021-05-05_hydrated_tweets_short.json",
"2021-05-09_hydrated_tweets_short.json"
]

    length_dct = {}
    length_dct['date'] = []
    length_dct['num tweets'] = []
    for filename in files:
        tweets_df = pre_process.read_file(filename)
        num_tweets = len(tweets_df)
        date_ = filename[:10]
        length_dct['date'].append(date_)
        length_dct['num tweets'].append(num_tweets)
    
    return pd.DataFrame(length_dct)

def pull_num_rec_csv():

    files = [
        "2021-01-01_cln.csv",
"2021-01-05_cln.csv",
"2021-01-09_cln.csv",
"2021-01-13_cln.csv",
"2021-01-17_cln.csv",
"2021-01-21_cln.csv",
"2021-01-25_cln.csv",
"2021-01-29_cln.csv",
"2021-02-02_cln.csv",
"2021-02-06_cln.csv",
"2021-02-10_cln.csv",
"2021-02-14_cln.csv",
"2021-02-18_cln.csv",
"2021-02-22_cln.csv",
"2021-02-26_cln.csv",
"2021-03-02_cln.csv",
"2021-03-06_cln.csv",
"2021-03-10_cln.csv",
"2021-03-14_cln.csv",
"2021-03-18_cln.csv",
"2021-03-22_cln.csv",
"2021-03-26_cln.csv",
"2021-03-30_cln.csv",
"2021-04-03_cln.csv",
"2021-04-07_cln.csv",
"2021-04-11_cln.csv",
"2021-04-15_cln.csv",
"2021-04-19_cln.csv",
"2021-04-23_cln.csv",
"2021-04-27_cln.csv",
"2021-05-01_cln2.csv",
"2021-05-05_cln.csv",
"2021-05-09_cln.csv"
    ]
    length_dct = {}
    length_dct['date'] = []
    length_dct['num vacc tweets'] = []
    for filename in files:
        tweets_df = pd.read_csv(filename, lineterminator='\n')
        num_tweets = len(tweets_df)
        date_ = filename[:10]
        length_dct['date'].append(date_)
        length_dct['num vacc tweets'].append(num_tweets)

    return pd.DataFrame(length_dct)

def comb_viz():

    tweets_by_day = pull_num_rec()
    vacc_tweets_by_day = pull_num_rec_csv()

    final_df = pd.merge(tweets_by_day, vacc_tweets_by_day, on='date', how='inner')
    final_df.loc[:, 'date'] = pd.to_datetime(final_df.loc[:, 'date'], format="%Y-%m-%d")

    return final_df
    
