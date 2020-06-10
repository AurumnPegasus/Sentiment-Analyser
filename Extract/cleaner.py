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

def remove_emoji(string):
    emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', string)

def write_sent(sent):
    cleaned = []
    for i in sent:
        s = ""
        for j in i[0]:
            j = str(j)
            j = j + " "
            s = s + j
        s = remove_emoji(s)
        element = [s, i[1]]
        cleaned.append(element)
    df = pd.DataFrame(cleaned)
    df.to_csv('cleaned_data.csv', index=False)

my_csv = extract_csv()
words = tokenize_tweets(my_csv)
sent = create_lemmatized_sent(words)
write_sent(sent)
