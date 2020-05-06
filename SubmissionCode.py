#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import arff, numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
b = arff.load(open('train_Y.arff'))
a = arff.load(open('train_X.arff'))
a=np.delete(a,0,0)
X_train, X_test, y_train, y_test = train_test_split( a, b, test_size = 0.3, random_state = 100)
dec = DecisionTreeClassifier()
dec.fit(X_train,Y_train)
y_pred=logreg.predict(X_test)
co=np.shape(X_test)[0]
y_pred.resize(co,1)
np.savetxt("predicted_test_Y.csv", y_pred, delimiter=",")

