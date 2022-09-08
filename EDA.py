#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Importing the necessary libraries 
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


#Load the data
df=pd.read_csv('Salaries.csv')


# In[3]:


df.describe()


# In[4]:


df.info()


# In[5]:


df.head()


# In[6]:


#Removing Null Values
new_df = df.dropna()
print(new_df)


# In[7]:


#Removing duplicated values 
print(df.duplicated())


# # Visualizations

# In[8]:


new_df.count()


# In[13]:


df.plot(x='job_title',y='salary')
plt.xlabel('job_title')
plt.ylabel('salary')


# In[20]:


df['remote_ratio'].plot(kind='hist')
plt.xlabel('remote_ratio')
plt.ylabel('Values')


# In[52]:


a=new_df['remote_ratio'].unique()
lab=['0','50','100']
print (a)

plt.pie(a,labels=lab)
plt.show()
plt.xlabel


# In[53]:


a=new_df['salary_in_usd']
print(a)

b=new_df['remote_ratio']

plt.scatter(a,b)


# In[54]:


new_df.corr()


# In[55]:


sns.heatmap(new_df.corr())


# In[ ]:





# In[ ]:





# In[ ]:




