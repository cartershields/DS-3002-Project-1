#!/usr/bin/env python
# coding: utf-8

# In[48]:


import json
import pandas as pd
import os
import numpy as np


# In[49]:


# Retrieve the local file

air = pd.read_csv('/Users/cartershields/Desktop/DS 3002/airbnb.csv')


# In[50]:


# Creating a summary for the data before transforming the data
shape = air.shape

# Number of Records
print('Number of observations = ', shape[1]*shape[0])

# Number of Columns
print('Number of columns = ', shape[1])


# In[51]:


# Deleting a column
# Deleting the country column because this dataset is for Airbnb's only in Amsterdam, so the country is always
# going to be the Netherlands

air.drop('country', inplace = True, axis = 1)


# In[52]:


# Creating a summary for the data after deleting the column
shape = air.shape

# Number of Records
print('Number of observations = ', shape[1]*shape[0])

# Number of Columns
print('Number of columns = ', shape[1])


# In[ ]:


# Choosing an output

# User input either JSON or CSV to write the updated file to a local file.
# If user tries to input another file type, throws an error that loops back to the user needing to input again.

input_type = input("Enter the file type you would like to output to:")

if input_type == 'CSV':
    data = os.path.join(os.getcwd())
    output_file = os.path.join(data, 'airbnb.csv')
    air.to_csv(output_file)
    print('File (CSV) outputted as "airbnb.csv"')
elif file_type == 'JSON':
    data = os.path.join(os.getcwd())
    output_file = os.path.join(data, 'airbnb.json')
    air.to_json(output_file)
    print('File (JSON) outputted as "airbnb.json"')
else:
    print('File type not found. Enter either CSV or JSON.')


# In[ ]:




