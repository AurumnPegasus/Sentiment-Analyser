import nltk
from nltk.tokenize import word_tokenize

f = open('text_data.txt', 'r+')
f1 = open('tweet_id.txt', 'w+')
data = f.read()

data = str(data)
data = word_tokenize(data)
tweet_id = []
tweet_sentiment = []
new_data = []

for i in data:
    i = str(i)
    if i[0].isdigit():
        new_data.append(i)

for i in range(0, len(new_data)):
    if(new_data[i][0] == '0' or new_data[i] == '1' or new_data[i][1] == '.'):
        tweet_sentiment.append(new_data[i])
    else:
        tweet_id.append(new_data[i])

for i in tweet_id:
    f1.write(i)
    f1.write("\n")

f.close()
f1.close()