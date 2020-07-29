#!/usr/bin/env python
# coding: utf-8

# In[1]:


port1={21:"FTP",22:'SSH',23:"telnet",80:'http'}
port1={value:key for key,value in port1.items()}
print(port1)


# In[2]:


list=[(1,2),(3,4),(5,6),(4,5)]
for i in range(len(list)):
     list[i]=sum(list[i])
print(list)


# In[5]:


lis=[(1,2,3),[1,2],['a','hit','less']]
ils=[x for i in lis for x in i]
print(ils)

