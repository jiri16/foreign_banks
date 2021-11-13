#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import pandas as pd
import numpy as np


# In[2]:


df = pd.read_csv('CH.csv',encoding = "ISO-8859-1")


# In[3]:


df=df.drop(['ï»¿region', 'incgroup','offshore','cntrycode','bankname 2009','spec','index_consol','cons_code','index_unconsol','unconsol_code','ISIN','Ticker','Swift','note_2009', 'note_2013', 'added2014', 'active2013','ownsou1995', 'ownsou1996', 'ownsou1997', 'ownsou1998', 'ownsou1999','ownsou2000', 'ownsou2001', 'ownsou2002', 'ownsou2003', 'ownsou2004','ownsou2005', 'ownsou2006', 'ownsou2007', 'ownsou2008', 'ownsou2009','ownsou2010', 'ownsou2011', 'ownsou2012', 'ownsou2013'], axis=1)


# In[4]:


df95 = df[df["own1995"] == 1]
df95 = df95[df95["yoe"] == 1995]
entries95 = pd.DataFrame(df95.country.value_counts()).rename(columns={"country": "entries95"})


# In[5]:


df96 = df[df["own1996"] == 1]
df96 = df96[df96["own1995"] != 1]
entries96 = pd.DataFrame(df96.country.value_counts()).rename(columns={"country": "entries96"})


# In[6]:


df97 = df[df["own1997"] == 1]
df97 = df97[df97["own1996"] != 1]
entries97 = pd.DataFrame(df97.country.value_counts()).rename(columns={"country": "entries97"})


# In[7]:


df98 = df[df["own1998"] == 1]
df98 = df98[df98["own1997"] != 1]
entries98 = pd.DataFrame(df98.country.value_counts()).rename(columns={"country": "entries98"})


# In[8]:


df99 = df[df["own1999"] == 1]
df99 = df99[df99["own1998"] != 1]
entries99 = pd.DataFrame(df99.country.value_counts()).rename(columns={"country": "entries99"})


# In[9]:


df00 = df[df["own2000"] == 1]
df00 = df00[df00["own1999"] != 1]
entries00 = pd.DataFrame(df00.country.value_counts()).rename(columns={"country": "entries00"})


# In[10]:


df01 = df[df["own2001"] == 1]
df01 = df01[df01["own2000"] != 1]
entries01 = pd.DataFrame(df01.country.value_counts()).rename(columns={"country": "entries01"})


# In[11]:


df02 = df[df["own2002"] == 1]
df02 = df02[df02["own2001"] != 1]
entries02 = pd.DataFrame(df02.country.value_counts()).rename(columns={"country": "entries02"})


# In[12]:


df03 = df[df["own2003"] == 1]
df03 = df03[df03["own2002"] != 1]
entries03 = pd.DataFrame(df03.country.value_counts()).rename(columns={"country": "entries03"})


# In[13]:


df04 = df[df["own2004"] == 1]
df04 = df04[df04["own2003"] != 1]
entries04 = pd.DataFrame(df04.country.value_counts()).rename(columns={"country": "entries04"})


# In[14]:


df05 = df[df["own2005"] == 1]
df05 = df05[df05["own2004"] != 1]
entries05 = pd.DataFrame(df05.country.value_counts()).rename(columns={"country": "entries05"})


# In[15]:


df06 = df[df["own2006"] == 1]
df06 = df06[df06["own2005"] != 1]
entries06 = pd.DataFrame(df06.country.value_counts()).rename(columns={"country": "entries06"})


# In[16]:


df07 = df[df["own2007"] == 1]
df07 = df07[df07["own2006"] != 1]
entries07 = pd.DataFrame(df07.country.value_counts()).rename(columns={"country": "entries07"})


# In[17]:


df08 = df[df["own2008"] == 1]
df08 = df08[df08["own2007"] != 1]
entries08 = pd.DataFrame(df08.country.value_counts()).rename(columns={"country": "entries08"})


# In[18]:


df09 = df[df["own2009"] == 1]
df09 = df09[df09["own2008"] != 1]
entries09 = pd.DataFrame(df09.country.value_counts()).rename(columns={"country": "entries09"})


# In[19]:


df10 = df[df["own2010"] == 1]
df10 = df10[df10["own2009"] != 1]
entries10 = pd.DataFrame(df10.country.value_counts()).rename(columns={"country": "entries10"})


# In[20]:


df11 = df[df["own2011"] == 1]
df11 = df11[df11["own2010"] != 1]
entries11 = pd.DataFrame(df11.country.value_counts()).rename(columns={"country": "entries11"})


# In[21]:


df12 = df[df["own2012"] == 1]
df12 = df12[df12["own2011"] != 1]
entries12 = pd.DataFrame(df12.country.value_counts()).rename(columns={"country": "entries12"})


# In[22]:


df13 = df[df["own2013"] == 1]
df13 = df13[df13["own2012"] != 1]
entries13 = pd.DataFrame(df13.country.value_counts()).rename(columns={"country": "entries13"})


# In[23]:


df_total = pd.concat([entries95,entries96,entries97,entries98,entries99,entries00,entries01,entries02,entries03,entries04,entries05,entries06,entries07,entries08,entries09,entries10,entries11,entries12,entries13], axis=1).fillna(0)
df_total


# In[24]:


df_total.to_csv("entries_total.csv")


# In[25]:


df_total.loc[df_total['entries95'] > 1, 'entries95'] = 1
df_total.loc[df_total['entries96'] > 1, 'entries96'] = 1
df_total.loc[df_total['entries97'] > 1, 'entries97'] = 1
df_total.loc[df_total['entries98'] > 1, 'entries98'] = 1
df_total.loc[df_total['entries99'] > 1, 'entries99'] = 1
df_total.loc[df_total['entries00'] > 1, 'entries00'] = 1
df_total.loc[df_total['entries01'] > 1, 'entries01'] = 1
df_total.loc[df_total['entries02'] > 1, 'entries02'] = 1
df_total.loc[df_total['entries03'] > 1, 'entries03'] = 1
df_total.loc[df_total['entries04'] > 1, 'entries04'] = 1
df_total.loc[df_total['entries05'] > 1, 'entries05'] = 1
df_total.loc[df_total['entries06'] > 1, 'entries06'] = 1
df_total.loc[df_total['entries07'] > 1, 'entries07'] = 1
df_total.loc[df_total['entries08'] > 1, 'entries08'] = 1
df_total.loc[df_total['entries09'] > 1, 'entries09'] = 1
df_total.loc[df_total['entries10'] > 1, 'entries10'] = 1
df_total.loc[df_total['entries11'] > 1, 'entries11'] = 1
df_total.loc[df_total['entries12'] > 1, 'entries12'] = 1
df_total.loc[df_total['entries13'] > 1, 'entries13'] = 1
df_total


# In[26]:


df_total.to_csv("entries_dummy.csv")


# In[ ]:




