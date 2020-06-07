import csv
from twython import Twython

CONSUMER_KEY = "MI2CPI8E9BQCWWxh0TA5Fe1vE"
CONSUMER_SECRET = "hpSul94tEYWq9KEHydOOjrm0zaerSpUnayxtA6w58IbkCXJJWJ"
OAUTH_TOKEN = "2456692051-5bU8nc0pqj868VAIPIBnb9MKITNp5kGxUJJnxHN"
OAUTH_TOKEN_SECRET = "Oe4SNNEqwa2vpzNLFwHclNJAU8mN9ERax3TVg082ad5Pd"
twitter = Twython(
    CONSUMER_KEY, CONSUMER_SECRET,
    OAUTH_TOKEN, OAUTH_TOKEN_SECRET)


with open('april28-june6.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)


f = open('data_set.txt', 'w+')
tweets = []
c  = 0
d = 0

for i in data:
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
