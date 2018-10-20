# read csv
dataset = read.csv('Salary_Data.csv')


# install.packages('caTools')
library(caTools)
# seed value to split
set.seed(123)
# splitRation is ration for training set, first argument is the dependent var(Y)
# return a list contain True/False means split, so for 10 data, 8 true and 2 false
split = sample.split(dataset$Salary, SplitRatio = 2/3)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

# fit linear regression to dataset
# lm used to fit linear models
regressor = lm(formula = Salary ~ YearsExperience,
               training_set)

#predit the test set results
y_pred = predict(regressor,newdata = test_set)


#visual train set result
#install.packages('ggplot2')
library(ggplot2)
ggplot() +
  geom_point(aes(x = training_set$YearsExperience, y = training_set$Salary),
             colour = 'red') +
  geom_line(aes(x = training_set$YearsExperience, y = predict(regressor,newdata = training_set)),
            colour = 'blue') +
  ggtitle('Salary Vs. YearsExperience (Train set)') +
  xlab('Years of Experience') +
  ylab('Salary')

#visual test set result
library(ggplot2)
ggplot() +
  geom_point(aes(x = test_set$YearsExperience, y = test_set$Salary),
             colour = 'red') +
  geom_line(aes(x = test_set$YearsExperience, y = predict(regressor,newdata = test_set)),
            colour = 'blue') +
  ggtitle('Salary Vs. YearsExperience (Test set)') +
  xlab('Years of Experience') +
  ylab('Salary')
