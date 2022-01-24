#!/usr/bin/env python
# coding: utf-8

# ## Importing Necessary Libraries

# In[47]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plot
import seaborn as sns
from pandas_profiling import ProfileReport


# In[43]:


from matplotlib.pyplot import *


# In[34]:


data = pd.read_csv('dataset_full(1).csv')


# In[35]:


data


# In[24]:


data.describe()


# In[25]:


data.info


# In[8]:


data. isnull()


# In[29]:


data.head()


# In[9]:


data.nunique()


# In[10]:


data.columns


# In[11]:


nan_value=data.isna().sum()
nan_value


# # checking the data imbalance

# In[38]:


ax= data.phishing.value_counts().plot.pie(autopct='%.2f')


# # How many Missing values in the dataset?

# In[12]:


for i in range(len(data.columns)):
    missing_data = data[data.columns[i]].isna().sum()
    perc = missing_data / len(data) * 100
    print(f'Feature {i+1} >> Missing entries: {missing_data}  |  Percentage: {round(perc, 2)}')


# In[26]:


plt.figure(figsize=(10,6))
sns.heatmap(data.isna(), cbar=False, cmap='viridis', yticklabels=False)


# Observation:
#     There  is no missing values in the dataset which is quite good 

# In[61]:


from pandas_profiling import ProfileReport
prof = ProfileReport(data)
prof.to_file(output_file='output.html')


# In[50]:



plot.figure()
plotnumber =1

for column in data.drop(['phishing'],axis=1):
    ax = plot.subplot(12,3,plotnumber)
    sns.countplot(data[column])
    plot.xlabel(column,fontsize=10)
    plotnumber+=1
plot.show()


# In[51]:


plot.figure()
plotnumber =1

for column in data.drop(['phishing'],axis=1):
    ax = plot.subplot(12,3,plotnumber)
    sns.violinplot(data= data,x=data[column],y =data["phishing"] )
    plot.xlabel(column,fontsize=10)
    plotnumber+=1
plot.show()


# In[30]:


plt.close();
sns.set_style("whitegrid");
sns.pairplot(data, hue="phishing",size=4)
plt.show()


# # checking the data imbalance

# In[39]:


sns.countplot(data['phishing'])


# In[52]:


ax= data.phishing.value_counts().plot.pie(autopct='%.2f')


# In[53]:


import numpy as np 
import pylab
import scipy.stats as stats


# In[58]:


plot.figure()
plotnumber =1

for column in data.drop(['phishing'],axis=1):
    stats.probplot(data, dist="norm", plot=pylab)
pylab.show()


# In[55]:




