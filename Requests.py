#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests

url = 'http://127.0.0.1:5000/predict'
r = requests.post(url,json={'GRE Score':339,'TOEFL Score':107,'University Rating':2.7,'SOP':3.37,                          'LOR':3.48,'CGPA':8.58,'Research':0.56})

print(r.json())

