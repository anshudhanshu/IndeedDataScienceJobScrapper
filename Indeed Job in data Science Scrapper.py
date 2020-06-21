#!/usr/bin/env python
# coding: utf-8

# ### Data Science Job Scrapper from indeed.com

# In[1]:


import pandas as pd
import requests
import numpy as np
from bs4 import BeautifulSoup


# In[179]:


df = pd.DataFrame(columns=['Title','Location','Remote','Company','Salary','Rating','Summary'])
for i in range(0,5000,10):
    response = requests.get('https://www.indeed.co.in/jobs?q=data+science&l=india&start='+str(i))
    soup = BeautifulSoup(response.content,'lxml')
    jobs=soup.findAll('div',attrs={'class':'result'})
    for job in jobs:
        try:
            title = job.find('a',attrs={'class':'jobtitle'})
            title=title.text.strip()
        except:
            title=np.nan
        try:
            location = job.find(['span','div'],attrs={'class':'location'})
            location=location.text.strip()
        except:
            location=np.nan
        try:
            remote=job.find('span',attrs={'class':'remote'})
            remote=remote.text.strip()
        except:
            remote=np.nan
        try:
            company=job.find('a',attrs={'class':'turnstileLink'})
            company=company.text.strip()
        except:
            company = np.nan
        try:
            salary=job.find('span',attrs={'class':'salaryText'})
            salary=salary.text.strip()
        except:
            salary=np.nan
        try:
            rating=job.find('span',attrs={'class':'ratingsContent'})
            rating=rating.text.strip()
        except:
            rating=np.nan
        try:
            summary=job.find('div',attrs={'class':'summary'})
            summary=summary.text.replace('\n','').strip()
        except:
            summary = np.nan
        df=df.append({'Title':title,'Location':location,'Remote':remote,'Company':company,'Salary':salary,'Rating':rating,'Summary':summary},ignore_index=True)
    print(df.shape)


# In[182]:


df.to_csv('dataScienceJobs.csv')


# In[ ]:


df.

