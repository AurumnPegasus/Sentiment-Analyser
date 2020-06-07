import pandas as pd
from pandas import Series

def extract_csv_text():
    my_filtered_csv = pd.read_csv('twitter_ids.csv', usecols=['id', 'text'])
    return my_filtered_csv

def create_dictionary():
    return pd.read_csv('april28-june6.csv', index_col=0, squeeze=True).to_dict()

def create_list(text_csv):
    id = text_csv.id.tolist()
    text = text_csv.text.tolist()
    tweet = []
    for i in range(0, len(id)):
        tweet.append([id[i], text[i]])
    return tweet

def convert_dict(tweet_dict, tweet_list):
    tweets = []
    for i in tweet_list:
        try:
            tweets.append([i[1], tweet_dict[i[0]]])
        except:
            pass
    return tweets

def write_data(tweets):
    f = open('data.txt', 'w+')
    for i in tweets:
        i = str(i) + "\n"
        f.write(i)
    f.close()

final_data = open('data.txt','a+')
text_csv = extract_csv_text()
tweet_dict = create_dictionary()
tweet_list = create_list(text_csv)
tweets = convert_dict(tweet_dict, tweet_list)
write_data(tweets)