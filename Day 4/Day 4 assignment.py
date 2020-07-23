#!/usr/bin/env python
# coding: utf-8

# In[6]:


print ("Question no1 :Write a code to Find all occurance of substring in the given string")


# In[4]:


import re
test_str ="onetwo three is one not onefour"
test_sub = "one"
print ("The original string is : " + test_str)
print ("The substring to find : " + test_sub)
res = [i.start() for i in re.finditer(test_sub , test_str)]
print ("The start indices of the substrings are : " + str(res))


# In[9]:


print ("Question2 :Write a code with different kind of strings with the help of islower() and isupper")


# In[21]:


str1 = "SNEHAL"
print (str1.isupper())
str2 = "SNEHAL03K"
print (str2.isupper())
str3 = "snehalK3"
print (str3.isupper())
str4 = "snehal.k"
print (str4.isupper())


# In[22]:


str1 = "snehal"
print (str1.islower())
str2 = "SNEhal"
print (str2.islower())
str3 = "snehalk"
print (str3.islower())
str4 = "sNEHAL2"
print (str4.islower())

