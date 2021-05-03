#!/bin/bash 

# Run via bash terminal with:
# sh hydrate_tweets.sh '2021-04-13'
# (replace date with desired file)

daily_dt=$1
source_file="data/${daily_dt}_clean-dataset-filtered.tsv"
dest_file="data/${daily_dt}_hydrated_tweets"

# 0. Create data/ folder if doesn't exist

if [[ ! -d data/ ]]; then
    echo "Creating data/ directory to store Twitter files"
    mkdir data/
else
    echo "data/ directory already exists"
fi


# 1. Download tsv.gz file from https://github.com/thepanacealab/covid19_twitter/tree/master/dailies

echo "1. Downloading unhydrated tweets for specified day: $daily_dt"

python download_unhydrated.py $daily_dt

echo "Stored unhydrated tweets in $source_file"


# 2a. Create api_keys.json if necessary

echo "2b. Create api_keys.json if necessary"

python create_api_key_json.py


# 2b. Hydrate tweets using get_metadata.py from https://github.com/thepanacealab/SMMT

echo "2b. Hydrate tweets for $daily_dt"

python get_metadata.py -i $source_file -o $dest_file -k api_keys.json -m e
#python get_metadata.py -i data/2021-04-14_clean-dataset-filtered.tsv -o data/2021-04-14_hydrated_tweets -k api_keys.json

echo "Stored hydrated tweets in $dest_file"