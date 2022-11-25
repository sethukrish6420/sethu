#!/usr/bin/env python
# coding: utf-8

# In[41]:


import pandas as pd


# In[42]:


print(pd.__version__)


# In[44]:


data = {'name' : ['sethu','krish','vijay'],
       'name2' : ['kavi','kalai','hari'],
       'name3' : ['kavi','kalai','hari'],
       'name4' : ['kavi','kalai','hari'],
       'name5' : ['kavi','kalai','hari'],
       'name6' : ['kavi','kalai','hari']}
print(data)


# In[45]:


df = pd.DataFrame(data)


# In[46]:


print(df)


# In[47]:


print(df.T)


# In[48]:


print(df.T.head())


# In[49]:


print(df.T.tail())


# In[50]:


print(len(df))


# In[51]:


print(len(df.T))


# In[52]:


print(df.index)


# In[53]:


print(df.loc[1])


# In[54]:


print(df.columns)


# In[55]:


print(df.T.loc[['name','name2']])


# In[56]:


print(df.reset_index)


# In[57]:


print(df.columns)


# In[58]:


print(df.T.columns)


# In[59]:


print(df['name'])


# In[60]:


print(df['name3'])


# In[61]:


print(df['name'].values)


# In[62]:


for name in df['name'].values:
    print(name)


# In[63]:


dff = df.drop(['name'],axis = 1)
print(dff)


# In[64]:


dff = df.drop(['name2'],axis= 1)
print(dff)


# In[65]:


print(df)


# In[66]:


dfff = df.drop(['name2'],axis = 1,inplace = True)
print(dfff)


# In[67]:


print(df)


# In[68]:


#import file


# In[69]:


import pandas as pd
import os
import glob


# In[70]:


name = pd.read_csv('titanic.csv',sep=",")


# In[71]:


print(name.columns)


# In[72]:


print(name.head())


# In[73]:


print(name.tail())


# In[74]:


print(name.loc[4])


# In[75]:


print(name.loc[[0,1]])


# In[76]:


print(name['Ticket'])


# In[79]:


print(name[['Ticket','Fare']])


# In[ ]:


# data query


# In[93]:


ds = pd.read_csv('titanic.csv')


# In[96]:


ds = ds.query("Sex == 'male' ")
print(ds)


# In[100]:


ds = pd.read_csv("titanic.csv")
ds = ds.query("Age >= 35 ")
print(ds)


# In[102]:


sd = ['male']
ds= ds.query("Sex in @sd")
print(ds)


# In[104]:


# merging data


# In[112]:


data1 = {'name':['sethu','krish','sugu','vijay','bavi'],
        'age' :[23,34,45,56,45]}
data1 = pd.DataFrame(data1)


# In[113]:


data2 = {'name':['kavi','bavi','guvi'],
        'age':[23,45,67]}
data2 = pd.DataFrame(data2)


# In[114]:


print(data1)
print(data2)


# In[115]:


result = data1.merge (data2,how = 'inner')
print(result)


# In[116]:


result = data1.merge(data2,how='outer')
print(result)


# In[117]:


result = data1.merge(data2,how = 'left')
print(result)


# In[118]:


result = data1.merge(data2,how = 'right')
print(result)


# In[119]:


result = data1.merge(data2,on ='age',how='inner')
print(result)


# In[121]:


result = data1.merge(data2,on =['age','name'],how = 'inner')
print(result)


# In[122]:


# series


# In[124]:


cs = {'day1': 230,'day2': 233,'day3':567}
ds= pd.Series(cs)
print(ds)


# In[129]:


s =[ 2,3,4]
fd = pd.Series(s,index = ["x","y","z"])
print(fd)


# In[130]:


list1 = ['python','csc']
list1 = pd.Series(list1)


# In[131]:


list2 = ['c++','java']
list2 = pd.Series(list2)


# In[132]:


result = pd.concat([list1,list2])
print(result)


# In[133]:


result = pd.concat([list1,list2],ignore_index= True)
print(result)


# In[134]:


#groupby


# In[135]:


rt = pd.read_csv('titanic.csv')


# In[137]:


tr = rt.groupby(['Cabin'])
print(tr.first())


# In[141]:


for group in tr:
    print(group[0])


# In[144]:


print(group[0],group[1],[['Sex','Ticket']])


# In[1]:


# pivot table


# In[2]:


import pandas as pd


# In[4]:


df = pd.read_csv('titanic.csv')
tb = pd.pivot_table(df,index = ['PassengerId','Ticket'])
print(tb)


# In[6]:


tb = pd.pivot_table(df,index = ['Ticket'])
print(tb)


# In[7]:


# datetime


# In[13]:


data = pd.date_range('1/10/2022',periods = 5,freq= 'H')
print(data)


# In[17]:


data = pd.date_range('11/01/2022',periods= 5, freq = 'D')
print(data)


# In[18]:


data = pd.date_range('2001',periods = 10,freq = 'Y')
print(data)


# In[19]:


data = pd.DataFrame()
data['date'] = pd.date_range('01/01/2000',periods = 10,freq = 'D')
print(data)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




