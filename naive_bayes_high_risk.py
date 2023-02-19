# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import f1_score
import categorypy as data

problem_categories = ['boiler heater', 'thermostat', 'supply', 'meter', 'account', 'payment', 'struggling to pay', 'high risk']
train_data = data.dataframe()# get the training data this should be a list of the phrases and which category they are in
train_values = pd.Series(train_data['Questions'])
train_results = pd.Series(train_data['Category'])

count_vec = CountVectorizer()
bow = count_vec.fit_transform(train_values.values.astype('U'))
bow = np.array(bow.todense())
X = bow
y = train_results

X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                                    test_size=0.2, 
                                                    stratify=y)

model = MultinomialNB().fit(X_train, y_train)

y_pred = model.predict(X_test)

print('Accuracy:', accuracy_score(y_test, y_pred))
print('F1 score:', f1_score(y_test, y_pred, average="macro"))
