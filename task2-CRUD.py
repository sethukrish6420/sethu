#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pymongo


# In[2]:


myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017")


# In[6]:


db = myclient['Database']


# In[7]:


mycol = mydb['Telephone_Directory']


# In[10]:


mydoc = ([
          {'name':'sethu','phone_num':1234567890,'address':'t.nagar,,chennai'},
          {'name':'krish','phone_num':9087654321,'address':'west_mambalam,,chennai'},
          {'name':'sugu','phone_num':9234567801,'address':'adyar,,chennai'},
          {'name':'vijay','phone_num':9102345678,'address':'tambaram,,chennai'}
])


# In[11]:


mycol.insert_many(mydoc)


# In[12]:


for x in mycol.find():
    print(x)


# In[25]:


myquery = {'address':'tambaram,,chennai'}
new = {"$set":{'address':'pallavaram,chennai'}}
mycol.update_one(myquery,new)


# In[26]:


for x in mycol.find():
    print(x)


# In[27]:


myquery = {'address':'pallavaram,chennai'}
mycol.delete_one(myquery)


# In[28]:


for x in mycol.find():
    print(x)


# In[ ]:




