import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.svm import LinearSVC

df = pd.read_csv('cleaned_data.csv')
tweets = []
train_txt = []
test_txt = []
test_sent = []
train_sent = []

txt = df.text.tolist()
sent = df.sentiment.tolist()


for i in range(0, 40000):
    if sent[i]>=0:
        sent[i] = 1
    else:
        sent[i] = 0
    tweets.append([txt[i], sent[i]])
    train_txt.append(txt[i])
    train_sent.append(sent[i])

for i in range(40000, len(txt)):
    if sent[i]>=0:
        sent[i] = 1
    else:
        sent[i] = 0
    tweets.append([txt[i], sent[i]])
    test_txt.append(txt[i])
    test_sent.append(sent[i])

ngram_vectorizer = CountVectorizer(binary=True, ngram_range=(1, 2))
ngram_vectorizer.fit(train_txt)
X = ngram_vectorizer.transform(train_txt)
X_test = ngram_vectorizer.transform(test_txt)

X_train, X_val, y_train, y_val = train_test_split(
    X, train_sent, train_size = 0.75
)

for c in [0.01, 0.05, 0.25, 0.5, 1]:
    
    svm = LinearSVC(C=c, max_iter=10000)
    svm.fit(X_train, y_train)
    print ("Accuracy for C=%s: %s" 
           % (c, accuracy_score(y_val, svm.predict(X_val))))


final_model = LinearSVC(C=0.5, max_iter=10000)
final_model.fit(X, train_sent)
print ("Final Accuracy: %s" 
       % accuracy_score(test_sent, final_model.predict(X_test)))

feature_to_coef = {
    word: coef for word, coef in zip(
        ngram_vectorizer.get_feature_names(), final_model.coef_[0]
    )
}
for best_positive in sorted(
    feature_to_coef.items(), 
    key=lambda x: x[1], 
    reverse=True)[:5]:
    print (best_positive)

for best_negative in sorted(
    feature_to_coef.items(), 
    key=lambda x: x[1])[:5]:
    print (best_negative)
    