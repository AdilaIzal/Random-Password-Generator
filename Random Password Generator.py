#!/usr/bin/env python
# coding: utf-8

# In[11]:


import random
passl = int(input("Please enter the length of password: "))
s = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM123456789!@#$%&6*_/"
p = "".join(random.sample(s,passl))
print(p)           

