#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


get_ipython().magic('matplotlib inline')


# In[4]:


recent_grads = pd.read_csv('recent-grads.csv')


# In[5]:


recent_grads.iloc[0]


# In[6]:


recent_grads.head()


# In[7]:


recent_grads.tail()


# In[8]:


recent_grads.describe()


# In[9]:


raw_data_count = recent_grads.shape[0]


# In[10]:


print(raw_data_count)


# In[11]:


recent_grads = recent_grads.dropna()


# In[12]:


cleaned_data_count = recent_grads.shape[0]


# In[13]:


print(cleaned_data_count)


# In[15]:


print(recent_grads.plot(x='Sample_size', y='Median', kind='scatter'))


# In[17]:


print(recent_grads.plot(x='Sample_size', y='Unemployment_rate', kind='scatter'))


# In[18]:


print(recent_grads.plot(x='Full_time', y='Median', kind='scatter'))


# In[19]:


print(recent_grads.plot(x='ShareWomen', y='Unemployment_rate', kind='scatter'))


# In[20]:


print(recent_grads.plot(x='Men', y='Median', kind='scatter'))


# In[21]:


print(recent_grads.plot(x='Women', y='Median', kind='scatter'))


# In[29]:


cols = ["Sample_size", "Median", "Employed", "Full_time", "ShareWomen", "Unemployment_rate", "Men", "Women"]
fig = plt.figure(figsize=(5,12))
for r in range(0, 4):
    ax = fig.add_subplot(4, 1, r+1)
    ax = recent_grads[cols[r]].plot(kind='hist', rot=90)


# In[30]:


cols = ["Sample_size", "Median", "Employed", "Full_time", "ShareWomen", "Unemployment_rate", "Men", "Women"]
fig = plt.figure(figsize=(5,12))
for r in range(4, 8):
    ax = fig.add_subplot(4, 1, r-3)
    ax = recent_grads[cols[r]].plot(kind='hist', rot=90)


# In[31]:


from pandas.plotting import scatter_matrix


# In[32]:


scatter_matrix(recent_grads[['Sample_size', 'Median']], figsize=(6,6))


# In[33]:


scatter_matrix(recent_grads[['Sample_size', 'Median', 'Unemployment_rate']], figsize=(10,10))


# In[36]:


recent_grads[:10].plot.bar(x='Major', y='ShareWomen', legend=False)
recent_grads[163:].plot.bar(x='Major', y='ShareWomen', legend=False)


# In[37]:


recent_grads[:10].plot.bar(x='Major', y='Unemployment_rate', legend=False)
recent_grads[163:].plot.bar(x='Major', y='Unemployment_rate', legend=False)


# In[ ]:




