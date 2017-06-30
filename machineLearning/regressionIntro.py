# https://www.youtube.com/watch?v=JcI5Vnw0b2c&index=2&list=PLQVvvaa0QuDfKTOs3Keq_kaG2P55YRn5v

import pandas as pd
import quandl
import math, datetime
import numpy as np
from sklearn import preprocessing, svm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from matplotlib import style
import pickle

df = quandl.get('WIKI/GOOGL')

df = df[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume']]
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Close']) / df['Adj. Close'] * 100.0
df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0

df = df[['Adj. Close', 'HL_PCT', 'PCT_change', 'Adj. Volume']]

forecast_col = 'Adj. Close'
df.fillna(-99999, inplace=True)

forecast_out = int(math.ceil(0.01*len(df)))
# print(forecast_out, 0.1*len(df))

df['label'] = df[forecast_col].shift(-forecast_out)
# print(df.head())

X = np.array(df.drop(['label'], 1))
X = preprocessing.scale(X)
X_lately = X[-forecast_out:]
X = X[:-forecast_out]


df.dropna(inplace=True)
y = np.array(df['label'])
# print(X, y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# clf = LinearRegression()
# clf.fit(X_train, y_train)
#
# with open('linearregression.pickle', 'wb') as f:
#     pickle.dump(clf, f)

pick_in = open('linearregression.pickle', 'rb')
clf = pickle.load(pick_in)

accuracy = clf.score(X_test, y_test)
print(accuracy)

forecast_set = clf.predict(X_lately)

print((forecast_set, accuracy, forecast_out))

df['Forecast'] = np.nan

last_date = df.iloc[-1].name
last_unix = last_date.timestamp()
one_day = 86400
next_unix = last_unix + one_day



