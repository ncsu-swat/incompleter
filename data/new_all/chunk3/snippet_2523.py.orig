#Source: https://stackoverflow.com/questions/73733871/typeerror-document-must-be-an-instance-of-dict-bson-son-son-bson-raw-bson-raw
from numpy.polynomial import Polynomial as poly 
import numpy as np
import matplotlib.pyplot as plt
import pymongo
import json
import pandas as pd

 
df = pd.read_csv(r'D:\polynomial\points.csv')
print(df)

x= np.array(df['Wavelength(A)'].tolist())
x= np.divide([299792.458], x)
y= np.array(df['Level(A)'].tolist())
x_trimmed = np.delete(x, np.where(y < 1e-4))
y_trimmed = np.delete(y, np.where(y < 1e-4))
test= poly.fit(x_trimmed, y_trimmed, 10)
print (test)

list1= test.convert().coef
print (list1)
print (len(list1))
#print (type(list1))
to_list= list1.tolist()
#print(to_list)
#data_format= json.dumps(to_list)
l = len(to_list)
#print (l)
mydict1= []
for i in range(l):
    mydict = { "a"+str(i) : to_list[i] }
    mydict1.append(mydict)
print (mydict1)


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["coefficients"]
x = mycol.insert_one(mydict1)