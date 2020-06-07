import csv
import pandas as pd
from twython import Twython

CONSUMER_KEY = "MI2CPI8E9BQCWWxh0TA5Fe1vE"
CONSUMER_SECRET = "hpSul94tEYWq9KEHydOOjrm0zaerSpUnayxtA6w58IbkCXJJWJ"
OAUTH_TOKEN = "2456692051-5bU8nc0pqj868VAIPIBnb9MKITNp5kGxUJJnxHN"
OAUTH_TOKEN_SECRET = "Oe4SNNEqwa2vpzNLFwHclNJAU8mN9ERax3TVg082ad5Pd"
twitter = Twython(
    CONSUMER_KEY, CONSUMER_SECRET,
    OAUTH_TOKEN, OAUTH_TOKEN_SECRET)



my_filtered_csv = pd.read_csv('twitter_ids.csv', usecols=['id', 'text'])

