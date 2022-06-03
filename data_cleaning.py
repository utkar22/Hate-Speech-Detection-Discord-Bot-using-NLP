import re
import pandas as pd
import csv

def clean_tweet(tweet):
    tweet = tweet.lower()
    tweet = re.sub(r"(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|^rt|http.+?", "", tweet)
    return tweet

output_file = open("op1.csv","w")
input_file_1 = open("train.csv", errors="ignore")
input_file_2 = open("labeled_data.csv", errors="ignore")

reader1 = csv.reader(input_file_1, delimiter = ',')
reader2 = csv.reader(input_file_2, delimiter = ',')

writer1 = csv.writer(output_file, delimiter = ',')

line_count = 0

for row in reader1:
    if line_count == 0:
        new_row = ["hate","offensive","tweet"]
    else:
        val = int(row[1])
        tweet = row[2]

        hate_val = val*3
        offensive_val = val*3
        tweet = clean_tweet(tweet)

        new_row = [hate_val, offensive_val, tweet]

    writer1.writerow(new_row)

    line_count+=1




line_count = 0

for row in reader2:
    if line_count == 0:
        pass
    else:
        count = int(row[1])
        hate = int(row[2])
        offensive = int(row[3])
        tweet = row[6]

        hate_val = int((hate/count)*3)
        offensive_val = int((offensive/count)*3)
        tweet = clean_tweet(tweet)

        new_row = [hate_val, offensive_val, tweet]
        writer1.writerow(new_row)

    line_count+=1


input_file_1.close()
input_file_2.close()
output_file.close()

f1 = open("op1.csv")
f2 = open("hate_speech.csv","w")

arr = f1.readlines()
f1.close()

for s in arr:
    if s == '\n':
        continue
    else:
        f2.write(s)

f2.close()

        
        
