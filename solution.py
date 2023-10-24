#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np


# In[5]:


def compute_cost(x,y,w,b):
    m = len(y)
    f = np.dot(w,x) + b
    cost = f - y
    cost = cost*cost # Makes the sqaure of elements 
    j = np.sum(cost)/(2*m)
    return j 


# In[ ]:


def compute_gradient(x,y,w,b):
    m = len(y)
    f = np.dot(w,x) + b
    del_jb = f - y
    del_jw = del_jb*x   # it will gives the element wise multiplication 
    del_jb_net = np.sum(del_jb)/m
    del_jw_net = np.sum(del_jw)/m
    return del_jb_net , del_jw_net

