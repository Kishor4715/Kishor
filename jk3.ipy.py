#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
a=np.array([1,6,2,7,6,4])
x=np.where(a==7)
print(x)


# In[4]:


import numpy as np
a=np.array([1,6,2,7,6,4])
x=np.where(a%3==1)
print(x)


# In[8]:


a=np.array([0,1,2,2,7,8,9])
b=np.searchsorted(a,8,side='right')
print(b)


# In[10]:


#sorting of an array
a=np.array([9,5,2,7,6,4])
print(np.sort(a))


# In[13]:


a=np.array([[7,4,9],[9,1,4]])
print(np.sort(a))


# In[19]:


#boolean indexing
import numpy as np 
a=np.array([31,78,69,100])
x=[True,True,True,True]
new=a[x]
print(x)
print(new)


# In[21]:


#filtering
a=np.array([31,78,69,100])
f=a>70
new=a[f]
print(f)
print(new)


# In[ ]:




