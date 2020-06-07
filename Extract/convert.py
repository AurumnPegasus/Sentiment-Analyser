import csv
from twython import Twython

CONSUMER_KEY = "<>"
CONSUMER_SECRET = "<>"
OAUTH_TOKEN = "<>"
OAUTH_TOKEN_SECRET = "<>"
twitter = Twython(
    CONSUMER_KEY, CONSUMER_SECRET,
    OAUTH_TOKEN, OAUTH_TOKEN_SECRET)


with open('april28-june6.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)


f = open('data_set.txt', 'a+')
tweets = []
c  = 0
d = 0

for j in range(10001, len(data)):
    i = data[j]
    tweet_id = i[0]
    d+=1
    print(d)
    if d == 10000:
        break
    try:
        tweet = twitter.show_status(id=tweet_id)
        text = tweet['text']
        tweets.append([text, i[1]])
        f.write(str([text, i[1]]) + "\n")
    except:
        pass

print(len(tweets))
f.close()
