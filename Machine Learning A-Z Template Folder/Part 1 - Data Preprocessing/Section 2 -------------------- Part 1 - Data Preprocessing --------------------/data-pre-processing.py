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
# categoyr by first column and all row
labelencoder_X = LabelEncoder()
X[:,0] = labelencoder_X.fit_transform(X[:,0])
onehotencoder_X = OneHotEncoder(categorical_features = [0])
X = onehotencoder_X.fit_transform(X).toarray()
labelencoder_Y = LabelEncoder()
Y = labelencoder_Y.fit_transform(Y)

# Split the dataset into the training set and test set
from sklearn.model_selection import train_test_split
# first is independent var, second is dependent var, third is test_size(20% of whole data set), train set is remain 80%, random_state is use for split sampling 
# relation between X and Y base on X -> Y
# test if X-test and Y_test follow predication
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 0)

# Feature Scaling
# because the data distribution on different dimension might have very large difference in range, so we neeed to scale data
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.fit_transform(X_test)