#!/usr/bin/env python
# coding: utf-8

# # Skusim scapenut IES stranku
# 

# In[52]:



import requests
from bs4 import BeautifulSoup
from time import sleep
from tqdm import tqdm
from IES_Downloader import IES_Downloader


# In[2]:



get_ipython().system('pip install tqdm')


# In[53]:


def getSoup(link):
    sleep(0.1) #to be kind to the website
    r = requests.get(link)
    r.encoding = 'UTF-8'
    return BeautifulSoup(r.text,'lxml')


# In[5]:


getSoup ('http://ies.fsv.cuni.cz/en/node/48')


# In[105]:



def getAllLinks(link):
    soup = getSoup(link)
    tds = soup.findAll('td', {'class':'peopleTableCellName'})
    return ['https://ies.fsv.cuni.cz' + td.find('a')['href'] for td in tds]

links = getAllLinks('http://ies.fsv.cuni.cz/en/node/48')


# In[106]:


def getName(link):
    soup = getSoup(link)
    return soup.find('h2').text
names = [getName(link) for link in links]


# In[47]:


def getPos(link):
    soup = getSoup(link)
    posis = soup.findAll('td',{'class':'peopleTableCellAcf'})    
    return posis 

Positions= getPos('http://ies.fsv.cuni.cz/en/node/48')   
  


# In[57]:


i=0;
for pos in Positions:        
    names[i]+' ' +pos.text;
    i=i+1;


# In[165]:






# In[134]:


"http://ies.fsv.cuni.cz/en/staff/barunik".split('/')[2]


# In[135]:


values = getMoreCharacteristics('https://ies.fsv.cuni.cz/en/staff/barunik', ['Phone:','Office:'])


# In[136]:


def getNextSiblingOfStrong(link,characteristic):
    soup = getSoup(link)
    strong = soup.find('strong',text=characteristic)
    return strong.next_sibling.strip()

def getMoreCharacteristics(link, characteristics):
    return [getNextSiblingOfStrong(link,char) for char in characteristics]



[getMoreCharacteristics(link,['Phone:','Office:']) for link in links[:2]]


# In[166]:


links;


# In[140]:


def getNextSiblingOfStrong(link,characteristic):
    soup = getSoup(link)
    strong = soup.find('strong',text=characteristic)
    return strong.next_sibling.strip()
[getNextSiblingOfStrong(link,'Phone:') for link in links[0:2]]


# In[167]:


def getCalendar(link): #{ 'td':'action'}
    soup=getSoup(link)
    table = soup.findAll('table',{ 'id':'caltable'})   
    strong = soup.find('a',text='Scheduled shutdown of servers')
    print(strong)
    
    getNextSiblingOfStrong
    
    
    print(table)    
    return [event.findAll('span') for event in table]

getCalendar('http://ies.fsv.cuni.cz/en/node/48')


# In[185]:


bf = getSoup('https://ies.fsv.cuni.cz/content/tree/index/lang/en')

bf.find_all('a',text='Scheduled shutdown of servers').parent.parent.parent.find('span')


# In[ ]:





# In[ ]:




