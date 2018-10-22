# read csv
dataset = read.csv('50_Startups.csv')

# Encoding categorical data
dataset$State = factor(dataset$State,
                         levels = c('New York', 'California', 'Florida'),
                         labels = c(1, 2, 3))

# install.packages('caTools')
library(caTools)
# seed value to split
set.seed(123)
# splitRation is ration for training set, first argument is the dependent var(Y)
# return a list contain True/False means split, so for 10 data, 8 true and 2 false
split = sample.split(dataset$R.D.Spend, SplitRatio = 0.8)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

#Fitting multiple linear regression to the train set
# regressor = lm( formula = Profit ~ R.D.Spend + Administration + Marketing.Spend + State)
# . means all independent variables
regressor = lm( formula = Profit ~ R.D.Spend,
                data = training_set)
summary(regressor)

#predit the test set results
y_pred = predict(regressor,newdata = test_set)