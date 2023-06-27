#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Clustering Music Genres

import pandas as pd
import numpy as np
from sklearn import cluster

data = pd.read_csv(r"C:\Users\Dhanu\Downloads\Clustering Music Genres\Spotify-2000.csv")
print(data.head())


# In[3]:


#drop the index column

data = data.drop("Index", axis=1)

print(data.corr())


# In[ ]:




