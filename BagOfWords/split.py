import pandas as pd

df = pd.read_csv('cleaned_data.csv', usecols=['text', 'sentiment'])

txt = df.text.tolist()
sent = df.sentiment.tolist()
tweets = []

for i in range(0, 10000):
    if sent[i]>=0:
        sent[i] = 0
    else:
        sent[i] = 1
    tweets.append([txt[i], sent[i]])


df = pd.DataFrame(tweets)
df.to_csv('testing_data.csv', index=False)

df = pd.read_csv('cleaned_data.csv', usecols=['text', 'sentiment'])

txt = df.text.tolist()
sent = df.sentiment.tolist()
tweets = []

for i in range(10000, 50000):
    if sent[i]>=0:
        sent[i] = 0
    else:
        sent[i] = 1
    tweets.append([txt[i], sent[i]])


df = pd.DataFrame(tweets)
df.to_csv('training_data.csv', index=False)
