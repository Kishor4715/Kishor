#!/usr/bin/env python
# coding: utf-8

# In[8]:


import numpy as np
a1=[10,20,30]
a2=[1,2,3]
a=np.array(a1)
b=np.array(a2)
print(a)
print(b)
print(a+b)
print(a-b)
print(a*b)
print(a//b)


# In[6]:


print(a.dot(b))
sclr=3
print(sclr)
print(a)
print(a*sclr)


# In[7]:


a=np.array([[10,20],[30,40]])
b=np.array([[3,7],[5,9]])
print(a%b)


# In[12]:


def my_fun(x,y):
    if x>y:
        return x-y
    else:
        return x+y
a1=[10,7,2]
a2=[6,5,3]
vf=np.vectorize(my_fun)
print(a1)
print(a2)
print(vf(a1,a2))

