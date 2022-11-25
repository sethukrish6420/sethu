#!/usr/bin/env python
# coding: utf-8

# In[55]:


import pymongo


# In[56]:


myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017/")


# In[57]:


mydb = myclient["database"]


# In[58]:


dblist = myclient.list_database_names()
print(dblist)


# In[59]:


mycollection = mydb["name list"]


# In[60]:


collist = mydb.list_collection_names()
print(collist)


# In[61]:


mydocument = {'name':'sethu',"add":"sidhi vinayagar kovil st"}


# In[62]:


x = mycollection.insert_one(mydocument)
print(x.inserted_id)


# In[63]:


for x in mycollection.find():
    print(x)


# In[64]:


collist = mydb.list_collection_names()
print(collist)


# In[65]:


# to write insert id


# In[66]:


mylist = ([
          {'name1':'sethu',"add1":"sidhi vinayagar kovil st"},
          {'name2':'sethu',"add2":"sidhi vinayagar kovil st"},
          {'name3':'sethu',"add3":"sidhi vinayagar kovil st"},
          {'name1':'sethu',"add1":"sidhi vinayagar kovil st"},
          {'name2':'sethu',"add2":"sidhi vinayagar kovil st"},
          {'name3':'sethu',"add3":"sidhi vinayagar kovil st"},
          {'name1':'sethu',"add1":"sidhi vinayagar kovil st"},
          {'name2':'sethu',"add1":"sidhi vinayagar kovil st"}])


# In[67]:


x = mycollection.insert_many(mylist);


# In[68]:


for x in mycollection.find():
    print(x)


# In[69]:


# write a id code


# In[70]:


x = mycollection.find_one()
print(x)


# In[71]:


for x in mycollection.find({},{"_id":0}):
    print(x)


# In[72]:


for x in mycollection.find({}, {'name':0,'add':1});
print(x) # get error because do not work 0, 1 at the same time


# In[ ]:


my_query = {'name':'sethu'}
for x in mycollection.find(my_query):
    print(x)


# In[ ]:


mylist2 = (
[
    {'name': 'sethu', 'add': 'sidhi vinayagar kovil st'},
    {'name': 'krish', 'add': '2,sidhi vinayagar kovil st'},
    {'name': 'vijay', 'add': '3sidhi vinayagar kovil st'},
    {'name': 'ajay', 'add': '4sidhi vinayagar kovil st'}
])


# In[ ]:





# In[ ]:


for x in mycollection.find().sort('name'):
    print(x)


# In[ ]:


for x in mycollection.find().sort('name',-1):
    print(x)


# In[ ]:


# delete


# In[ ]:


my_query = {'name':'sethu'}
mycollection.delete_one(my_query)
for x in mycollection.find():
    print(x)


# In[ ]:


my_query = {'name1':'sethu'}
mycollection.delete_many(my_query)
for x in mycollection.find():
    print(x)


# In[ ]:


mycollection.delete_many({})
for x in mycollection.find():
    print(x)


# In[ ]:


mylist = ([
          {'name1':'sethu',"add1":"sidhi vinayagar kovil st"},
          {'name2':'sethu',"add2":"sidhi vinayagar kovil st"},
          {'name3':'sethu',"add3":"sidhi vinayagar kovil st"},
          {'name1':'sethu',"add1":"sidhi vinayagar kovil st"},
          {'name2':'sethu',"add2":"sidhi vinayagar kovil st"},
          {'name3':'sethu',"add3":"sidhi vinayagar kovil st"},
          {'name1':'sethu',"add1":"sidhi vinayagar kovil st"},
          {'name2':'sethu',"add1":"sidhi vinayagar kovil st"}])
mycollection.insert_many(mylist)
for x in mycollection.find():
    print(x)


# In[ ]:


# update


# In[ ]:


my_query = {'name1':'sethu'}
new_value = {"$set":{'age':23}}
mycollection.update_one(my_query,new_value)
for x in mycollection.find():
    print(x)


# In[ ]:


my_query = {'name1':'sethu'}
new_value = {"$set":{'age':23}}
mycollection.update_many(my_query,new_value)
for x in mycollection.find():
    print(x)
    


# In[ ]:


x = mycollection.update_many(my_query,new_value)
print(x.modified_count)


# In[ ]:


my_query = {'name2':'sethu'}
newvalue = {"$set":{'add2':'t nagar'}}
mycollection.update_many(my_query,newvalue)
for x in mycollection.find():
    print(x)


# In[ ]:


for x in mycollection.find().limit(5):
    print(x)


# In[ ]:





# In[ ]:




