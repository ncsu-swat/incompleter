#Source: https://stackoverflow.com/questions/62772575/typeerror-argument-must-be-a-string-or-number-on-column-with-strings-that-are-n
import numpy as np #mathematical tools
import matplotlib.pyplot as plt #plot nice charts
import pandas as pd #import and manage data sets

# Making a list of missing value types
missing_values = ["?"]
df= pd.read_csv('D:\\data.csv',na_values = missing_values)

#print the new table with the missing values 
# print (df)
# print (df.isnull())


X = df.iloc[:, :-1].values #Matrix - independent variables (features)
y = df.iloc[:, 24].values #dependent variables vectors


from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X2 = LabelEncoder()
X[:, 2] = labelencoder_X2.fit_transform(X[:, 2]) #gas=0, fuel=1 

labelencoder_X3 = LabelEncoder()
X[:, 3] = labelencoder_X3.fit_transform(X[:, 3])

#I get an error her
labelencoder_X4 = LabelEncoder()
X[:, 4] = labelencoder_X4.fit_transform(X[:, 4])

labelencoder_X5 = LabelEncoder()
X[:, 5] = labelencoder_X5.fit_transform(X[:,5])

labelencoder_X6 = LabelEncoder()
X[:, 6] = labelencoder_X6.fit_transform(X[:, 6])

labelencoder_X7 = LabelEncoder()
X[:, 7] = labelencoder_X7.fit_transform(X[:, 7])

labelencoder_X13 = LabelEncoder()
X[:, 13] = labelencoder_X13.fit_transform(X[:, 13])

labelencoder_X14 = LabelEncoder()
X[:, 14] = labelencoder_X14.fit_transform(X[:, 14])

labelencoder_X15 = LabelEncoder()
X[:, 16] = labelencoder_X14.fit_transform(X[:, 16])

from sklearn.impute import SimpleImputer
imputer=SimpleImputer(missing_values="NaN", strategy='mean')
imputer.fit(X[:, 1:24])  
X[:, 1:24]=imputer.transform(X[:, 1:24])