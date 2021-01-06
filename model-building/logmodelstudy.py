#!/usr/bin/env python
# coding: utf-8

# In[17]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
import pickle

from sklearn.model_selection import train_test_split as tts
from sklearn.utils import resample
from sklearn.linear_model import LogisticRegression

warnings.filterwarnings('ignore')


# In[2]:


df = pd.read_csv("train.csv")


# In[3]:


df2 = pd.get_dummies(df, drop_first=True)


# In[4]:


X = df2[['Age', 'Previously_Insured', 'Gender_Male', 'Vehicle_Age_> 2 Years', 'Vehicle_Damage_Yes', 'Vehicle_Age_< 1 Year']]
y = df2[['Response']]


# In[8]:


X_train, X_val, y_train, y_val = tts(X, y, test_size=.05, random_state=42)


# In[9]:


df3 = X_train.copy()


# In[10]:


df3['Response'] = y_train


# In[12]:


df3_majority = df3[df3['Response'] == 0]
df3_minority = df3[df3['Response'] == 1]


# In[13]:


df3_majority_downsampled = resample(df3_majority, replace=False, n_samples = len(df3_minority), random_state=42)


# In[14]:


df3_downsampled = pd.concat([df3_majority_downsampled, df3_minority])


# In[15]:


X_train_downsampled = df3_downsampled.drop('Response', axis = 1)


# In[16]:


y_train_downsampled = df3_downsampled.Response


# In[18]:


logmodel = LogisticRegression()


# In[19]:


logmodel.fit(X_train_downsampled, y_train_downsampled)


# In[20]:


prediction_logmodel = logmodel.predict(X_val)


# In[21]:


pickle.dump(logmodel, open('logmodelml.pkl', 'wb'))

