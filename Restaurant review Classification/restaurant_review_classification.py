# -*- coding: utf-8 -*-
"""Restaurant Review Classification.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1fnV3ZgO-HrnRUBD0eZQODO1jBUDk8nUM

# Data Preprocessing

Dataset : https://www.kaggle.com/datasets/akram24/restaurant-reviews

## Importing libraries and dataset
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dataset = pd.read_csv('/content/Restaurant_Reviews.tsv', delimiter = '\t' ,quoting = 3)

"""## Data Exploration

"""

dataset.head()

dataset.shape

dataset.info()

dataset.columns

dataset.describe()

"""## Dealing with missing values"""

dataset.isnull().values.any()

dataset.isnull().values.sum()

"""## Countplot"""

sns.countplot(x= 'Liked',data = dataset)

# positive review
(dataset.Liked== 1).sum()

# negative review
(dataset.Liked== 0).sum()

"""## Length of messages"""

dataset.head()

dataset['Length'] = dataset['Review'].apply(len)

dataset.head()

# Histogram
dataset['Length'].plot(bins = 100,kind = 'hist')

dataset.Length.describe()

# Longest message
dataset[dataset["Length"] == 149]['Review'].iloc[0]

# Shortest message
dataset[dataset["Length"] == 11]['Review'].iloc[0]

positive = dataset[dataset['Liked'] == 1]

negative = dataset[dataset['Liked'] == 0]

positive

negative

dataset.head()

"""## Cleaning the text"""

import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

corpus = []

for i in range(0,1000):
  review = re.sub('[^a-zA-Z]',' ', dataset['Review'][i])
  review = review.lower()
  review = review.split()

  ps = PorterStemmer()
  all_stopwords = stopwords.words('english')
  all_stopwords.remove('not')
  review = [ps.stem(word) for word in review if not word in set(all_stopwords)]
  review  = ' '.join(review)
  corpus.append(review)

print(corpus)

len(corpus)

"""## Cleaning the bag of words"""

from sklearn.feature_extraction.text import CountVectorizer

cv= CountVectorizer(max_features= 1500)

dataset.head()

x= cv.fit_transform(corpus).toarray()
y = dataset.iloc[:,1]

x.shape

y.shape

"""## Splitting the dataset"""

from sklearn.model_selection import train_test_split
x_train, x_test,y_train,y_test = train_test_split(x,y,test_size = 0.2)

x_train.shape

x_test.shape

y_train.shape

y_test.shape

"""# Building the model

## Naive Bayes
"""

from sklearn.naive_bayes import GaussianNB
classifier_nv = GaussianNB()
classifier_nv.fit(x_train,y_train)

y_pred = classifier_nv.predict(x_test)

from sklearn.metrics import accuracy_score, confusion_matrix

acc= accuracy_score(y_test,y_pred)

acc

cm = confusion_matrix(y_test,y_pred)

cm

"""## XGBoost classifier"""

from xgboost import XGBClassifier
classifier_xgb = XGBClassifier()
classifier_xgb.fit(x_train,y_train)

y_pred = classifier_xgb.predict(x_test)

from sklearn.metrics import accuracy_score, confusion_matrix

acc= accuracy_score(y_test,y_pred)

acc

cm = confusion_matrix(y_test,y_pred)

cm

"""# Final Model"""

from xgboost import XGBClassifier
classifier = XGBClassifier()
classifier.fit(x_train,y_train)

y_pred = classifier.predict(x_test)

from sklearn.metrics import accuracy_score, confusion_matrix

acc= accuracy_score(y_test,y_pred)

acc

cm = confusion_matrix(y_test,y_pred)

cm