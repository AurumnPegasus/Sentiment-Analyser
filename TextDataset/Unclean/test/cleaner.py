import nltk
import re
import googletrans
import langdetect
from googletrans import Translator
from langdetect import detect

c = 0

tweets_raw = []
f = open('cleaned_data.txt', 'w+')

with open('data.txt','r') as file:      
    for line in file:   
        tweets_raw.append(line)

tweets_english = []
tweets_hindi = []
c = 0

for i in tweets_raw:

    i = str(i)
    i = re.sub('(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*(\?[a-z\_\=\&\;\-]*))',' ', i)
    i = re.sub('(@[A-Za-z0-9]+)', ' ', i)
    i = re.sub('(&[A-Za-z]*\;)', ' ', i)
    try:
        lang = detect(i)
        if lang == "en" :
            tweets_english.append(i)
        elif lang == "hi" :
            tweets_hindi.append(i)
    except:
        pass

print(len(tweets_english))

for i in tweets_english:
    f.write(i)

f.close()