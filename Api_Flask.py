#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, jsonify, request
import joblib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score


# In[ ]:


model = joblib.load('model.pkl')
app = Flask(__name__)


@app.route("/")
def nothello():
    return "Welcome to machine learning model APIs!"
@app.route("/index")
def hello():
    return "Fool!"
@app.route("/predict", methods=['GET','POST'])
def predict():
     json_ = request.json
     query_df = pd.DataFrame(json_)
     query = pd.get_dummies(query_df)
     prediction = model.predict(query)
     return jsonify({'prediction': list(prediction)})

if __name__ == '__main__':
    app.run(debug=False)


# In[ ]:




