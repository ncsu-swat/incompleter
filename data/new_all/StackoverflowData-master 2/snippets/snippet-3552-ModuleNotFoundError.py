#Source: https://stackoverflow.com/questions/72333214/attributeerror-nonetype-object-has-no-attribute-get-and-the-knn-step-is-ri
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.multiclass import OneVsRestClassifier
from sklearn.neighbors import KNeighborsClassifier

from tkinter import * 
top = Tk('300','300')
box= Text(top).grid(row=1,column=1)
p = TfidfVectorizer(sublinear_tf=True, stop_words='english')
p.fit(box.get("1.0",END))
wordOfp = p.transform(p)

x_train,x_test,y_train,y_test = train_test_split(wordOfp,y,random_state = 42, test_size = 0.2)# y is target
model = OneVsRestClassifier(KNeighborsClassifier(n_neighbors=5, metric= 'euclidean'  ))
model.fit(x_train,y_train)
prediction = model.predict(x_test)