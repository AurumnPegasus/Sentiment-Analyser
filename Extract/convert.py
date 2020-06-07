import csv
import pandas as pd

my_filtered_csv = pd.read_csv('twitter_ids.csv', usecols=['id', 'text'])
