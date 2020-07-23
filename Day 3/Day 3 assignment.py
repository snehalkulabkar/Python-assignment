#!/usr/bin/env python
# coding: utf-8

# In[26]:


print ("Question1: sum of n no with while loop")


# In[27]:


print ("question2: take a integer and find prime or not")


# In[30]:


n = int(input("Enter n number you want for sum:"))
sum1 = 0
while(n > 0):
    sum1=sum1+n
    n=n-1
print("the sum of n no is",sum1)


# In[48]:


num = int(input("Enter a no: "))
for i in range (2, num):
    if num %i==0:
        print("not a prime no")
    else :
        print("Prime no")


# In[ ]:




