#!/usr/bin/env python
# coding: utf-8

# In[1]:


import yahoo_fin
import requests
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
from yahoo_fin import stock_info as si
import urllib
import string
import urllib.request 
from urllib.request import urlopen
import http.cookiejar


# In[2]:


#taking input ticker
ticker= input("Enter Ticker: ")


# In[3]:


quote_table = si.get_quote_table(ticker)
quote_table


# In[4]:


#input 1- Earnings Per Share (Trailing Twelve Months)
eps= quote_table['EPS (TTM)']
print(eps)
type(eps)


# In[5]:


# Create an URL object
url = 'https://ycharts.com/companies/'+ticker+'/pe_ratio'
agent = {"User-Agent":'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
page = requests.get(url, headers=agent)
# parser-lxml = Change html to Python friendly format
# Obtain page's information
soup = BeautifulSoup(page.content, 'lxml')
#soup


# Obtain information from tag <table>
table1 = soup.find_all('div', {'class': 'key-stat-title'})

print(table1)
headers = []
for i in table1:
    title = i.text
    headers.append(title)


# In[6]:


#input 2- 5 year historical Average Price to Earning Ratio
str1 = headers[2].strip()
fyhap = float(str1)
print(fyhap)
type(fyhap)


# In[7]:


analyst_info=si.get_analysts_info(ticker)
analyst_info


# In[8]:


#input 3- Expected Growth Rate
exp_growth_rate=analyst_info['Growth Estimates'][ticker][4]
exp_gr=exp_growth_rate[:-1]
exp_gr=float(exp_gr)
print(exp_gr)
cons_gr= (1-0.25)*exp_gr
cons_gr=cons_gr/100
cons_gr


# In[9]:


#Putting it all together
five_year_value=eps*fyhap*(1+cons_gr)**5
five_year_value


# In[10]:


#discount factor
#taking discount factor to be 9%
today_value=five_year_value/((1+0.09)**5)
today_value


# In[ ]:




