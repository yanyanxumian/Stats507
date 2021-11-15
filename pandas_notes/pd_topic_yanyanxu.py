# jupyter:
#   jupytext:
#     cell_metadata_json: true
#     notebook_metadata_filter: markdown
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.11.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# ## Topics in Pandas
# **Stats 507, Fall 2021** 
#   

# ## Contents
# Add a bullet for each topic and link to the level 2 title header using 
# the exact title with spaces replaced by a dash. 
#
# + [Topic Title](#Topic-Title) 
# + [Topic 2 Title](#Topic-2-Title)

# ## Topic Title
# Include a title slide with a short title for your content.
# Write your name in *bold* on your title slide. 


#!/usr/bin/env python
# coding: utf-8

# **Name：Yan Xu
# 
# Unique Name:yanyanxu
# 
# Email:yanyanxu@umich.edu

# In[ ]:


import pandas as pd
import numpy as np
from datetime import datetime
from ps1_solution import ci_prop
import numpy.random as npra
from warnings import warn
import matplotlib.pyplot as plt
from os.path import exists


# In[ ]:


from scipy import stats
from scipy.stats import chi2_contingency 
from IPython.display import HTML


# ## Empty cells
# 
# Remove rows: remove rows that contain empty cells. Since data sets can be very big, and removing a few rows will not have a big impact on the result.
# Replace Empty Values:insert a new value using fillna() to replace NA.
# Replace Only For a Specified Columns: To only replace empty values for one column, specify the column name for the DataFrame.

# In[ ]:


#If you want to consider inf and -inf to be “NA” in computations
pd.options.mode.use_inf_as_na = True


# In[ ]:


df = pd.read_csv('https://www.w3schools.com/python/pandas/dirtydata.csv.txt')
df #The dataframe containing bad data we want to clean


# To make detecting missing values easier (and across different array dtypes), pandas provides the isna() and notna() functions, which are also methods on Series and DataFrame objects

# In[ ]:


df["Date"][20:25].notna()


# In[ ]:


new_df = df.dropna()
print(new_df.to_string())#dropna() method returns a new DataFrame, and will not change the original.
#If you want to change the original DataFrame, use the `inplace = True` argument


# In[ ]:


#insert a new value to replace the empty values
df.fillna(130)
df["Calories"].fillna(130, inplace = True)#only replace empty values for one column


# ## Data in wrong format
# 
# In our Data Frame, we have two cells with the wrong format.
# Check out row 22 and 26, the 'Date' column should be a string that represents a date,try to convert all cells in the 'Date' column into dates.

# Method to validate a date string format in Python

# In[ ]:


date_string = '12-25-2018'
format = "%Y/%m/d"

try:
  datetime.strptime(date_string, format)
  print("This is the correct date string format.")
except ValueError:
  print("This is the incorrect date string format. It should be YYYY/MM/DD")


# This is the incorrect date string format. It should be YYYY/MM/DD

# In[ ]:


# for row 26,the "date" column is in wrong format
df['Date'] = pd.to_datetime(df['Date'])


# ## Removing Duplicates
# 
# Duplicate rows are rows that have been registered more than one time.
# To discover duplicates, we can use the duplicated() method.
# The duplicated() method returns a Boolean values for each row.

# In[ ]:


print(df[10:15].duplicated())


# To remove duplicates, use the drop_duplicates() method.

# In[ ]:


df.drop_duplicates(inplace = True)

