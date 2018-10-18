# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 19:01:46 2018

@author: yul04
"""

# import librarys
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# read csv to dataset
dataset = pd.read_csv('Data.csv')
# iloc, : means all, first parameyter is row, second is column
# X contail all values except last column
X = dataset.iloc[:,:-1].values
# Y contain last column
Y = dataset.iloc[:,-1].values

# pre-processsing data by change missing value to mean of other value
from sklearn.preprocessing import Imputer
# define what kind of missing value, in which strategy, axis = 0 means take mean for column, =1 for take mean of row
imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)
# fit imputer to X
imputer = imputer.fit(X[:,1:3])
X[:,1:3] = imputer.transform(X[:,1:3])

# Encoding categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder()
X[:,0] = labelencoder_X.fit_transform(X[:,0])
onehotencoder_X = OneHotEncoder(categorical_features = [0])
X = onehotencoder_X.fit_transform(X).toarray()
labelencoder_Y = LabelEncoder()
Y = labelencoder_Y.fit_transform(Y)
