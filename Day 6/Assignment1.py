#!/usr/bin/env python
# coding: utf-8

# In[3]:


print ("Asiignment1 : Covert two list into dictionary in one lone code using list comprehension")


# In[2]:


list1 = [1,2,3,4,5,7,8]
list2 = ["a", "b", "c", "d", "e", "f", "g"]
res = {list1[i]: list2[i] for i in range(len(list1))} 
print ("Result in dictionary is : " +  str(res)) 

