#!/bin/bash 

filename="full_dates.txt"

while read date
do
echo $date
sh hydrate_tweets.sh $date
done < $filename