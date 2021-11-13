#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import os


# In[5]:


df = pd.read_csv('sovereign rating.csv')


# In[6]:


df


# In[7]:


condition1 = [
    (df['Agency'] == "Fitch") &(df['Rating'] == "C") ,
    (df['Agency'] == "Fitch") &(df['Rating'] == "CCC-") ,
    (df['Agency'] == "Fitch") &(df['Rating'] == "CCC"),
    (df['Agency'] == "Fitch") &(df['Rating'] == "B-"),
    (df['Agency'] == "Fitch") &(df['Rating'] == "B"),
    (df['Agency'] == "Fitch") &(df['Rating'] == "B+") ,
    (df['Agency'] == "Fitch") &(df['Rating'] == "BB-") ,
    (df['Agency'] == "Fitch") &(df['Rating'] == "BB"),
    (df['Agency'] == "Fitch") &(df['Rating'] == "BB+"),
    (df['Agency'] == "Fitch") &(df['Rating'] == "BBB-"),
    (df['Agency'] == "Fitch") &(df['Rating'] == "BBB") ,
    (df['Agency'] == "Fitch") &(df['Rating'] == "BBB+") ,
    (df['Agency'] == "Fitch") &(df['Rating'] == "A-"),
    (df['Agency'] == "Fitch") &(df['Rating'] == "A"),
    (df['Agency'] == "Fitch") &(df['Rating'] == "A+"),
    (df['Agency'] == "Fitch") &(df['Rating'] == "AA-") ,
    (df['Agency'] == "Fitch") &(df['Rating'] == "AA") ,
    (df['Agency'] == "Fitch") &(df['Rating'] == "AA+"),
    (df['Agency'] == "Fitch") &(df['Rating'] == "AAA"),
    ]


# In[8]:


values1 = [5, 15, 20, 25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100]


# In[9]:


df['rate1'] = np.select(condition1, values1)


# In[10]:


condition2 = [
    (df['Agency'] == "Moody's") &(df['Rating'] == "Ca") ,
    (df['Agency'] == "Moody's") &(df['Rating'] == "Caa3") ,
    (df['Agency'] == "Moody's") &(df['Rating'] == "Caa2"),
    (df['Agency'] == "Moody's") &(df['Rating'] == "Caa1"),
    (df['Agency'] == "Moody's") &(df['Rating'] == "B3"),
    (df['Agency'] == "Moody's") &(df['Rating'] == "B2") ,
    (df['Agency'] == "Moody's") &(df['Rating'] == "B1") ,
    (df['Agency'] == "Moody's") &(df['Rating'] == "Ba3"),
    (df['Agency'] == "Moody's") &(df['Rating'] == "Ba2"),
    (df['Agency'] == "Moody's") &(df['Rating'] == "Ba1"),
    (df['Agency'] == "Moody's") &(df['Rating'] == "Baa3") ,
    (df['Agency'] == "Moody's") &(df['Rating'] == "Baa2") ,
    (df['Agency'] == "Moody's") &(df['Rating'] == "Baa1"),
    (df['Agency'] == "Moody's") &(df['Rating'] == "A3"),
    (df['Agency'] == "Moody's") &(df['Rating'] == "A2"),
    (df['Agency'] == "Moody's") &(df['Rating'] == "A1") ,
    (df['Agency'] == "Moody's") &(df['Rating'] == "Aa3") ,
    (df['Agency'] == "Moody's") &(df['Rating'] == "Aa2"),
    (df['Agency'] == "Moody's") &(df['Rating'] == "Aa1"),
    (df['Agency'] == "Moody's") &(df['Rating'] == "Aaa")
    ]


# In[11]:


values2 = [5, 10, 15, 20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100]


# In[12]:


df["rate2"] = np.select(condition2, values2)


# In[13]:


df


# In[14]:


condition3 = [
    (df['Agency'] == "Standard & Poor's") &(df['Rating'] == "CC") ,
    (df['Agency'] == "Standard & Poor's") &(df['Rating'] == "CCC-") ,
    (df['Agency'] == "Standard & Poor's") &(df['Rating'] == "CCC"),
    (df['Agency'] == "Standard & Poor's") &(df['Rating'] == "CCC+"),
    (df['Agency'] == "Standard & Poor's") &(df['Rating'] == "B-"),
    (df['Agency'] == "Standard & Poor's") &(df['Rating'] == "B") ,
    (df['Agency'] == "Standard & Poor's") &(df['Rating'] == "B+") ,
    (df['Agency'] == "Standard & Poor's") &(df['Rating'] == "BB-") ,
    (df['Agency'] == "Standard & Poor's") &(df['Rating'] == "BB"),
    (df['Agency'] == "Standard & Poor's") &(df['Rating'] == "BB+"),
    (df['Agency'] == "Standard & Poor's") &(df['Rating'] == "BBB-"),
    (df['Agency'] == "Standard & Poor's") &(df['Rating'] == "BBB") ,
    (df['Agency'] == "Standard & Poor's") &(df['Rating'] == "BBB+") ,
    (df['Agency'] == "Standard & Poor's") &(df['Rating'] == "A-"),
    (df['Agency'] == "Standard & Poor's") &(df['Rating'] == "A"),
    (df['Agency'] == "Standard & Poor's") &(df['Rating'] == "A+"),
    (df['Agency'] == "Standard & Poor's") &(df['Rating'] == "AA-") ,
    (df['Agency'] == "Standard & Poor's") &(df['Rating'] == "AA") ,
    (df['Agency'] == "Standard & Poor's") &(df['Rating'] == "AA+"),
    (df['Agency'] == "Standard & Poor's") &(df['Rating'] == "AAA"),
    ]


# In[15]:


values3 = [5, 10, 15, 20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100]


# In[16]:


df["rate3"] = np.select(condition3, values3)


# In[17]:


df


# In[18]:


df["rate"]=df["rate1"] + df["rate2"] + df["rate3"]


# In[19]:


df=df.drop(columns=['rate1', 'rate2','rate3'])


# In[20]:


df1 = df.groupby(['Date','country']).mean()


# In[21]:


df1.to_csv("ahoj.csv")


# In[ ]:




