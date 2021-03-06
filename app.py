#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
data = pd.read_csv("startup.csv")
x = data.iloc[:,0:-2]
y = data.iloc[:,-1]
from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest = train_test_split(x,y,test_size=0.25,random_state=42)
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(xtrain,ytrain)


# In[ ]:


from flask import Flask , render_template , request
app = Flask(__name__)
@app.route('/')
def xyza():
    return render_template("startup.html")
@app.route('/startup',methods = ['get','post'])
def xxx():
    if request.method=='POST':
        x1 = int(request.form['a'])
        y1 = int(request.form['b'])
        z1 = int(request.form['c'])
        x2=[[x1,y1,z1]]
        ypred = model.predict(x2)
        print(ypred)
        
    return render_template("startup.html",profit=ypred)

if __name__ == "__main__":
    app.run()

