# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 14:04:03 2020

@author: vidhu sharma
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""Load data from csv files"""

cell_df = pd.read_csv(r"C:\Users\vidhu sharma\Downloads\A.I\cell_samples.csv")
print(cell_df.tail())
print(cell_df.shape)
print(cell_df.size)
print(cell_df.count)
print(cell_df['Class'].value_counts)

"""Distribution of the classes"""

benign_df = cell_df[cell_df['Class']==2][0:200]
malignant_df = cell_df[cell_df['Class']==4][0:200]

axes = benign_df.plot(kind='scatter', x='Clump', y='UnifSize', color='blue', label='Benign')
malignant_df.plot(kind='scatter', x='Clump', y='UnifSize', color='red', label='Benign', ax=axes)

"""Identifying Unwanted rows"""

print(cell_df.dtypes)

cell_df = cell_df[pd.to_numeric(cell_df['BareNuc'], errors='coerce').notnull()]
cell_df['BareNuc'] = cell_df['BareNuc'].astype('int')
print(cell_df.dtypes)

"""Identifying Unwanted columns"""

print(cell_df.columns)

feature_df = cell_df[['Clump','UnifSize','UnifShape','MargAdh','SingEpiSize','BareNuc','BlandChrom','NormNucl','Mit']]
#cell_df 100 rows and 11 columns,
#picked 9 columns out of 11

#Independent var
X= np.asarray(feature_df)

#Dependent var
y= np.asarray(cell_df['Class'])

print(y[0:5])

"""Divide the data as train dataset"""

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=4)

#546x9
print(X_train.shape)
#546x1
print(y_train.shape)
#137x9
print(X_test.shape)
#137x1
print(y_test.shape)

"""Modelling SVM"""

from sklearn import svm

classifier = svm.SVC(kernel='linear', gamma='auto', C=2)
classifier.fit(X_train, y_train)

y_predict = classifier.predict(X_test)

"""Evaluation"""

from sklearn.metrics import classification_report 

print(classification_report(y_test, y_predict))