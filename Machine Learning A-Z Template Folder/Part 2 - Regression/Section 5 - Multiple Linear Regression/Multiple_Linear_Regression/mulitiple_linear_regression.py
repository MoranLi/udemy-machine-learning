# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 15:45:49 2018

@author: yul04
"""

# import librarys
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# read csv to dataset
dataset = pd.read_csv('50_Startups.csv')
# iloc, : means all, first parameyter is row, second is column
# X contail all values except last column
X = dataset.iloc[:,:-1].values
# Y contain last column
Y = dataset.iloc[:,-1].values


# Encoding categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
# categoyr by first column and all row
labelencoder_X = LabelEncoder()
X[:,3] = labelencoder_X.fit_transform(X[:,3])
onehotencoder_X = OneHotEncoder(categorical_features = [3])
X = onehotencoder_X.fit_transform(X).toarray()

# Avoid the dummy variable trap
X = X[:,1:] 

# Split the dataset into the training set and test set
from sklearn.model_selection import train_test_split
# first is independent var, second is dependent var, third is test_size(20% of whole data set), train set is remain 80%, random_state is use for split sampling 
# relation between X and Y base on X -> Y
# test if X-test and Y_test follow predication
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 0)

# Fitting Mulitiple Linear Regression to the Train Set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train,Y_train)

# Predicting hte Test set Results
Y_pred = regressor.predict(X_test)

# Building the optimal model using backward elimination
import statsmodels.formula.api as sm
X = np.append(arr = np.ones((50,1)).astype(int), values = X, axis = 1)

'''
# Feature Scaling
# because the data distribution on different dimension might have very large difference in range, so we neeed to scale data
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.fit_transform(X_test)
'''