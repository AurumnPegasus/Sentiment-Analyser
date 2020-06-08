import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
import nltk 
import string
import re

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

pd.set_option('display.max_colwidth', 100)

def load_data():
    data = pd.read_csv('data.csv')
    return data

tweet_df = load_data()
tweet_df.head()

print('Dataset size:',tweet_df.shape)
print('Columns are:',tweet_df.columns)

tweet_df.info()


filename = 'data.csv'
file = open(filename, 'rt')
text = file.read()
file.close()

words = text.split()

string.punctuation
#print(string.punctuation)

# split into words
tokens = word_tokenize(text)

# convert to lower case
tokens = [w.lower() for w in tokens]

# remove punctuation from each word
table = str.maketrans('', '', string.punctuation)
stripped = [w.translate(table) for w in tokens]

# remove all tokens that are not alphabetic
words = [word for word in stripped if word.isalpha()]

# filter out stop words
stop_words = set(stopwords.words('english'))
words = [w for w in words if not w in stop_words]

print(words[:100])

#table = str.maketrans('', '', string.punctuation)
#stripped = [w.translate(table) for w in words]
#print(stripped[:100])


stop_words = stopwords.words('english')
print(stop_words)
