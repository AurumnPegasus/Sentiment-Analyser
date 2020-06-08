import nltk
import pandas as pd
import re
import string
from nltk.tokenize import WordPunctTokenizer
from nltk.tag import pos_tag
from nltk.stem.wordnet import WordNetLemmatizer 
from nltk.corpus import stopwords

def extract_csv():
    my_filtered_csv = pd.read_csv('data.csv', usecols=['text', 'sentiment'])
    return my_filtered_csv

def tokenize_tweets(my_csv):
    tweets = my_csv.text.tolist()
    sentiments = my_csv.sentiment.tolist()
    tokenizer = WordPunctTokenizer() 
    cleaned = []
    for i in range(0, len(tweets)):
        text = tweets[i]
        text = re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+#]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+','', text)
        text = re.sub("(@[A-Za-z0-9_]+)","", text)
        text = tokenizer.tokenize(text)
        element = [text, sentiments[i]]
        cleaned.append(element)
    return cleaned

def lemmatize_sentence(tweet_tokens, stop_words = ()):
    lemmatizer = WordNetLemmatizer()
    cleaned_tokens = []
    for token, tag in pos_tag(tweet_tokens):
        if tag.startswith('NN'):
            pos = 'n'
        elif tag.startswith('V'):
            pos = 'v'
        else:
            pos = 'a'
        token = lemmatizer.lemmatize(token, pos)
        if len(token) > 0 and token not in string.punctuation and token.lower() not in stop_words:
            cleaned_tokens.append(token.lower())
    return cleaned_tokens

def create_lemmatized_sent(words):
    cleaned = []
    stop_words = stopwords.words('english')
    for i in range(0, len(words)):
        sent = lemmatize_sentence(words[i][0], stop_words)
        if len(sent) > 0:
            element = [sent, words[i][1]]
            cleaned.append(element)
    return cleaned

def write_sent(sent):
    cleaned = []
    for i in sent:
        s = ""
        for j in i[0]:
            j = str(j)
            j = j + " "
            s = s + j
        element = [s, i[1]]
        cleaned.append(element)
    df = pd.DataFrame(cleaned)
    df.to_csv('cleaned_data.csv', index=False)

my_csv = extract_csv()
words = tokenize_tweets(my_csv)
sent = create_lemmatized_sent(words)
write_sent(sent)
