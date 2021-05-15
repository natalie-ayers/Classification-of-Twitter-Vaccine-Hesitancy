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



