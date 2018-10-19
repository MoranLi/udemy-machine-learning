# read csv
dataset = read.csv('Data.csv')

# handle missing data
# for ifelse, first parameter is if the data is missing(NaN)
# second parameter is use ave function to calculate average
#   the first parateter for ave is the data
#   second parameter is function actually calculate mean, na.rm = True so it take NaN as one element
# third parameter is if data is not NaN
dataset$Age = ifelse(is.na(dataset$Age),
                     ave(dataset$Age, FUN = function(x) mean(x,na.rm = TRUE)),
                     dataset$Age)
dataset$Salary = ifelse(is.na(dataset$Salary),
                        ave(dataset$Salary, FUN = function(x) mean(x,na.rm = TRUE)),
                        dataset$Salary)
dataset$Country = factor(dataset$Country,
                         levels = c('France','Spain','Germany'),
                         labels = c(1,2,3))
dataset$Purchased = factor(dataset$Purchased,
                         levels = c('Yes','No'),
                         labels = c(1,0))

# install.packages('caTools')
library(caTools)
# seed value to split
set.seed(123)
# splitRation is ration for training set
# return a list contain True/False means split, so for 10 data, 8 true and 2 false
split = sample.split(dataset$Purchased, SplitRatio = 0.8)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

training_set[,2:3] = scale(training_set[,2:3])
test_set[,2:3] = scale(test_set[,2:3])
