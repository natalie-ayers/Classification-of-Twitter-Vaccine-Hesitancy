# ml-for-pp_vaccine-hesitancy

Primary Repository Contents:

lda_topics.ipynb
  Primary notebook for performing LDA modeling and analysis. Configured to perform Gensim or MALLET LDA and create visualizations including wordclouds, PyLDAvis, and seaborn plots.
  
pipeline.py
  Contains script for grid search of Gensim and MALLET LDA models.
  
download_unhydrated.py
  Contains script to download unhydrated tweets from www.panacealab.org/covid19/ and hydrate to contain full tweet content. Script developed and modified from instructions provided: https://github.com/thepanacealab/covid19_twitter/blob/master/COVID_19_dataset_Tutorial.ipynb. Produces zip file containing metadata of each tweet and json of full tweet contents among other files. 
  
pre_process.py
  Script to clean, tokenize, and filter for vaccine-related tweets
