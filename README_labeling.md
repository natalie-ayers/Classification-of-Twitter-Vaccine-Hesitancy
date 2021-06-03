<<<<<<< HEAD
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
=======
# Downloading zip files from Google Drive using Google API
1. Place the client_secret json file as 'credentials.json' in 'creds' directory in the same directry as driver.py  
2. Place 'folder_ID.txt' in the same directry as driver.py  
3. (Only first run) Run 'python driver.py'. It will show you the link first, click on it and choose an appropriate account. Once logged-in, 'token.pickle' file is automatically generated and stores the authenticate information.  
  If it does not work in the second run: remove token.pickle and run driver.py again.
4. Run 'python driver.py'. 

# Interpreting VADER score  
positive: compound score>=0.05  
neutral: compound score between -0.05 and 0.05  
negative: compound score<=-0.05  
https://predictivehacks.com/how-to-run-sentiment-analysis-in-python-using-vader/  

# TROUBLE SHOOTING  
- 'Error tokenizing data. C error: Buffer overflow caught - possible malformed input file.' https://intellipaat.com/community/19314/error-in-reading-a-csv-file-in-pandas-cparsererror-error-tokenizing-data-c-error-buffer-overflow-caught-possible-malformed-input-file  

>>>>>>> b9d79cb1b8a80eb726ce742664a7d790309d7024
