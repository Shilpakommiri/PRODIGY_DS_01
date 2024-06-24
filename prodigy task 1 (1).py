#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


df=pd.read_csv("world_population.csv")


# In[4]:


df


# In[5]:


df.head()


# In[6]:


df.tail()


# In[8]:


df.shape


# In[10]:


df.columns


# In[12]:


df.dtypes


# In[13]:


df.info()


# In[15]:


df.describe()


# In[16]:


df.duplicated().sum()


# In[17]:


df.isna().sum().any()


# In[18]:


df=df.fillna(method="ffill")
df.head()


# In[21]:


df['Country/Territory'].unique()


# In[22]:


df['CCA3'].unique()


# In[23]:


df.head()


# In[33]:


cols=['2022 Population', '2020 Population',
       '2015 Population', '2010 Population', '2000 Population',
       '1990 Population', '1980 Population', '1970 Population']


# df.columns

# In[36]:


for i in cols:
    fig = plt.figure(figsize=(5,5))
    plt.hist(df[i],color='#B22222',bins=10)
    plt.xlabel(i)
    plt.show()


# In[41]:


years=df.columns[5:14]
total_values=df[years].sum()
plt.figure(figsize=(5,5))
plt.barh(years,total_values,color='#000000')
plt.xlabel('total_values')
plt.ylabel('years',size=20)
plt.title('Total values per year', size=20)
plt.show()


# In[42]:


country_by_1970 = df.sort_values(by='1970 Population').head(10)


# In[43]:


country_by_1970


# In[54]:


country_by_1970_t = country_by_1970.set_index('Country/Territory').T
for country_name, data_values in country_by_1970.T.iterrows():
    fig=plt.figure(figsize=(10,5))
    sns.barplot(x=data_values.index, y=data_values.values)
    


# In[51]:


country_by_2022 = df.sort_values(by='2022 Population').head(10)


# In[52]:


country_by_2022


# In[53]:


country_by_2022_t = country_by_2022.set_index('Country/Territory').T
for country_name, data_values in country_by_2022.T.iterrows():
    fig=plt.figure(figsize=(10,5))
    sns.barplot(x=data_values.index, y=data_values.values)
    plt.xlabel('Countries')
    plt.ylabel('Data values')
    plt.title(f"(country_name) - Data values from 1970 to 2022")
    


# In[ ]:




