#!/usr/bin/env python
# coding: utf-8

# In[35]:


print ("sort an array and move all zero at end")


# In[32]:


def move_zero(num_list):
    a = [0 for i in range(num_list.count(0))]
    x = [ i for i in num_list if i != 0]
    x.extend(a)
    return(x)
print(move_zero([10,0,11,12,0,14,17]))


# In[37]:


print ("merge sorted list1 and list2 combined it to form one sorted list")


# In[34]:


list1 = [1, 5, 6, 9, 11] 
list2 = [3, 4, 7, 8, 10] 
print ("The original list 1 is : " + str(list1)) 
print ("The original list 2 is : " + str(list2)) 
size1 = len(list1) 
size2 = len(list2) 

res = [] 
i, j = 0, 0
while i < size_1 and j < size2: 
    if list1[i] < list2[j]: 
      res.append(list1[i]) 
      i += 1

    else: 
      res.append(list2[j]) 
      j += 1
res = res + list1[i:] + list2[j:] 
print ("The combined sorted list is : " + str(res)) 

