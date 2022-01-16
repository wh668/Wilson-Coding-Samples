# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 19:19:10 2021

@author: Wilso
"""

import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import scale
from sklearn.metrics import plot_confusion_matrix

'''
Taking a look at some relationships between differnet features...
As one might expect, the scaled and concatenated feature linking runs with ERA produced
the larget R^2 value (Score a lot of runs and don't give up many = Win!!!). 
'''
# Read data into dataframe
df = pd.read_csv(r"C:\Users\Wilso\Downloads\baseballdatabank-master\baseballdatabank-master\core\Teams.csv")

# Lose all columns where Division Win is nan
df = df[df.DivWin.notna()]

# Dropping column since it is the lone column holding many nan values
df.drop(['WCWin'], axis=1, inplace=True)
df.dropna(inplace=True)

categorical = []

# Collect all columns holding non numeric data
for i in range(0, df.shape[1]):
    col = df.iloc[[0],[i]][df.iloc[[0],[i]].columns[0]].tolist()[0]
    if not isinstance(col, int) and not isinstance(col, float):
        categorical.append(df.columns[i])
categorical.remove('WSWin')

# Build correct input and output data scaled
y = df['WSWin'].copy()
X = df.drop('WSWin', axis=1).copy()
X_encoded = pd.get_dummies(X, columns=categorical)
X1 = X.drop(categorical, axis=1).copy()

# Create training/testing data
X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.3)
X_train_scaled = scale(X_train)
X_test_scaled = scale(X_test)

# Support Vector Machines classifier and confusion matrix
svc = SVC()
svc.fit(X_train_scaled, y_train)
plot_confusion_matrix(svc, X_test_scaled, y_test, values_format='d',
                      display_labels = ['Dis Not Win WS', 'Won WS'])
      
# KNN classifier and confusion matrix              
kn = KNeighborsClassifier(n_neighbors = 5, metric = 'minkowski', p = 2)
kn.fit(X_train_scaled, y_train)
plot_confusion_matrix(kn, X_test_scaled, y_test, values_format='d',
                      display_labels = ['Dis Not Win WS', 'Won WS'])

# Gaussian Naive Bayes classifier and confusion matrix
gnb = GaussianNB()
gnb.fit(X_train_scaled, y_train)
plot_confusion_matrix(gnb, X_test_scaled, y_test, values_format='d',
                      display_labels = ['Dis Not Win WS', 'Won WS'])

# Logistic Regression classifier and confusion matrix
lr = LogisticRegression()
lr.fit(X_train_scaled, y_train)
plot_confusion_matrix(lr, X_test_scaled, y_test, values_format='d',
                      display_labels = ['Dis Not Win WS', 'Won WS'])

# Random Forest classifier and confusion matrix
rf = RandomForestClassifier()
rf.fit(X_train_scaled, y_train)
plot_confusion_matrix(rf, X_test_scaled, y_test, values_format='d',
                      display_labels = ['Dis Not Win WS', 'Won WS'])