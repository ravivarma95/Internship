#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[2]:


from bs4 import BeautifulSoup
import requests


# In[3]:


Page = requests.get('https://en.wikipedia.org/wiki/Main_Page')


# In[4]:


page


# In[5]:


soup = BeautifulSoup(Page.content)


# In[6]:


Page


# In[7]:


soup


# In[68]:


hdrs = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8'])
hdrs


# In[83]:


all_headers = []
for i in soup.find_all('span', class_= "mw-headline"):

    all_headers.append(i.text)


# In[88]:


all_headers


# In[ ]:




