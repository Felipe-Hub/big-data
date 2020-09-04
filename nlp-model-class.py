import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

df = pd.read_csv('data.csv')
X = df['Message']
y = df['Category']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

cv = CountVectorizer()

X_train = cv.fit_transform(X_train)
X_test = cv.transform(X_test)

model = MultinomialNB()
model.fit(X_train, y_train)


import pickle

vectorizer = "vectorizer.pkl"

with open(vectorizer, 'wb') as file:
  pickle.dump(cv, file)
  
model_file = "spam_classifier.pkl"

with open(model_file, 'wb') as file:
  pickle.dump(model, file)
