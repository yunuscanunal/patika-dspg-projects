#!/usr/bin/env python
# coding: utf-8

# In[28]:


def reverse_liste(liste):
    for i in liste:
        i.reverse()
    liste.reverse()
    return liste


# In[ ]:


#Testing


# In[33]:


girdi= [[1, 2], [3, 4], [5, 6, 7]]
çıktı= [[7, 6, 5], [4, 3], [2, 1]]


# In[41]:


check = reverse_liste(girdi)


# In[43]:


check == çıktı


# In[ ]:




