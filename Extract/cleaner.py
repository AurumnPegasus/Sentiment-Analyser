import nltk
import pandas as pd

read_file = pd.read_csv (r'temp_data.txt', header = None)
read_file.columns = ['text','sentiment']
read_file.to_csv (r'unclean_tweets.csv', index=None)
