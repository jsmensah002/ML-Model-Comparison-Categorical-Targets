#Importing file using pandas
import pandas as pd
df = pd.read_csv('Bank_Churn.csv')
print(df)

#Dataset requires no cleaning
#The aim of this project is to build a model predict whether a customer would churn using key variables and do a cross validation

#Changing columns into dummy variables
geo_dummies = pd.get_dummies(df['Geography'], dtype=float)
gender_dummies = pd.get_dummies(df['Gender'],dtype=float)
print(geo_dummies)
print(gender_dummies)

#Defining x and y variables
x = pd.concat([gender_dummies,
               geo_dummies,
               df['CreditScore'],
               df['Age'],
               df['Tenure']],axis='columns')

y = df['Exited']
print(x)
print(y)

#Defining variables for prediction
geography = 'Spain'
gender = 'Male'

row = pd.DataFrame(0.0,index=[0],columns=x.columns)
row.loc[0,geography] = 1
row.loc[0,gender] = 1
row.loc[0, 'CreditScore'] = 940
row.loc[0,'Age'] = 44
row.loc[0,'Tenure'] = 6

#Importing SVC
from sklearn.svm import SVC
svm = SVC()
svm.fit(x,y)

#Prediction test 
prediction = svm.predict(row)[0]
print(prediction)

#Train test method
from sklearn.model_selection import train_test_split as tt
x_train,x_test,y_train,y_test = tt(x,y,test_size=0.2,random_state=42)
svm.fit(x_train,y_train)

#Checking the performance
score = svm.score(x,y)
train_score = svm.score(x_train,y_train)
test_score = svm.score(x_test,y_test)
print(score)
print(train_score)
print(test_score)

