import nltk

def tokenize(tweets):
    clean = []

    for i in tweets:
        i = list(i)
        i = i[2:-3]
        print(i)
        break



f = open('data.txt', 'r+')
tweets = f.readlines()
tweets = tokenize(tweets)