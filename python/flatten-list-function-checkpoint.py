#!/usr/bin/env python
# coding: utf-8

# In[38]:


f_liste = list()
def flat_liste(liste):
    
    for i in liste:
        if type(i) == list:
            flat_liste(i)
        else:
            f_liste.append(i)


# In[39]:


# Testing


# In[40]:


girdi = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
çıktı = [1,'a','cat',2,3,'dog',4,5]
flat_liste(girdi)
print(f_liste)


# In[41]:


f_liste == çıktı

