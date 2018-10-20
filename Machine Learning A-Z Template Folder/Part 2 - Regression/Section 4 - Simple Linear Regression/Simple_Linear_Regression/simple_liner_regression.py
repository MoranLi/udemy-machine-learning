# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 16:29:38 2018

@author: yul04
"""

# import librarys
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# read csv to dataset
dataset = pd.read_csv('Salary_Data.csv')
# iloc, : means all, first parameyter is row, second is column
# X contail all values except last column
X = dataset.iloc[:,:-1].values
# Y contain last column
Y = dataset.iloc[:,1].values

# Split the dataset into the training set and test set
from sklearn.model_selection import train_test_split
# first is independent var, second is dependent var, third is test_size(20% of whole data set), train set is remain 80%, random_state is use for split sampling 
# relation between X and Y base on X -> Y
# test if X-test and Y_test follow predication
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 1/3, random_state = 0)

# make simple linear regression model base on train set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train,Y_train)

# predict test set result
Y_pred = regressor.predict(X_test)

#visualising the train set result
plt.scatter(X_train,Y_train,color = 'red')
plt.plot(X_train,regressor.predict(X_train),color = 'blue')
plt.title('Salary Vs. Expreience (Training Set)')
plt.xlabel('Year of Experience')
plt.ylabel('Salary')
plt.show()

#visualising the train set result
plt.scatter(X_test,Y_test,color = 'red')
plt.plot(X_test,regressor.predict(X_test),color = 'blue')
plt.title('Salary Vs. Expreience (Test Set)')
plt.xlabel('Year of Experience')
plt.ylabel('Salary')
plt.show()


# Feature Scaling
# because the data distribution on different dimension might have very large difference in range, so we neeed to scale data
'''
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.fit_transform(X_test)
'''