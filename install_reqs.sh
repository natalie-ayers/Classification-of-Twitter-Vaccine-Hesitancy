#!/bin/bash 

# Not yet functional requirements.txt
# pip install -r requirements.txt


wget https://raw.githubusercontent.com/thepanacealab/SMMT/master/data_acquisition/get_metadata.py -O get_metadata.py

wget https://raw.githubusercontent.com/thepanacealab/SMMT/master/data_preprocessing/parse_json_lite.py -O parse_json_lite.py
echo "After downloading parse_json_lite.py, replace pd.io.json.json_normalize(data) in line 67 with pd.json_normalize(data)"

wget https://raw.githubusercontent.com/thepanacealab/SMMT/master/data_preprocessing/fields.py -O fields.py