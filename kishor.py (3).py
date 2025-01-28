#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
a=np.array([10,20,30,40])
print("1 D array",a)


# In[5]:


import numpy as np
a=np.array([[10,20,30,40],[30,40,60,790]])
print("2 D array:\n",a)


# In[7]:


import numpy as np
a=np.array([[10,20,30,40],[2,3,4,56],[30,40,60,790]])
print("3 D array:\n",a)


# In[9]:


import numpy as np
a=np.zeros((3,5))
print("\n array with zeros:\n",a)


# In[10]:


import numpy as np
a=np.random.random((2,3))
print("\n Random value:\n",a)


# In[18]:


import numpy as np
a= np.arange(20,60,5)
print("\nSequence array:\n",a)


# In[23]:


import numpy as np
g=np.array ([[10,20,56,67],[60,90,98,70],[90,9,98,100]])
h=g.reshape(4,3)
print("\n Orginal array:\n",g,"\n Reshaped array:\n",h)


# In[25]:


import numpy as np
a=np.array([[10,20,30],[30,40,50],[40,90,88]])
f=a.flatten()
print("orginal array:\n",a)
print("flatten array:\n",f)


# In[43]:


import numpy as np
a=np.array([[[[[[10]]]]]])
print("\n Dimensions;\n",a.ndim)
print("\n Shape of the array:\n",a.shape)


# In[44]:


import numpy as np
a=np.array([[[[[[10]]]]]])
print('/ntype:\n',a.dtype)


# In[45]:


import numpy as np
a=np.array([[10,20,30],[30,40,50],[40,90,88]])
s=len(a)
print('\nsize\n',s)


# In[3]:


import numpy as np
a=[1,2,3]
a=np.array(a)
n=a.astype('float64')
print(a)
print(n)
print(n.dtype)


# In[6]:


import numpy as np
a=np.array([1,2,3,4,5,6,7,8,9])
s=a[2:6]
print(s)


# In[11]:


import numpy as np
a=np.array([1,2,3,4,5,6,7,8,9])
s=a[::4]
print(s)


# In[15]:


import numpy as np
a=np.array([1,2,3,4,5,6,7,8,9])
s=a[8:3:-3]
print(s)


# In[23]:


import numpy as np
a=np.array([[10,20,30],[40,60,79],[90,98,88]])
print("2 D array:\n",a)
s=a[0:2,1:3]
print(s)


# In[25]:


import numpy as np
a=np.array([[10,20,30],[40,60,79],[90,98,88]])
print("2 D array:\n",a)
c1=a[:,0]
print("Output:",c1)


# In[26]:


import numpy as np
a=np.array([[10,20,30],[40,60,79],[90,98,88]])
print("2 D array:\n",a)
c1=a[0,:]
print("Output:",c1)


# In[27]:


import numpy as np
a=np.array([[10,20,30],[40,60,79],[90,98,88]])
print("2 D array:\n",a)
c1=a[0:2:1]
print("Output:",c1)


# In[29]:


import numpy as np
import array 
arr=array.array('i',[10,20,30,40,50])
print(arr[0])    
print(arr[3])    


# In[34]:


import numpy as np
import array 
arr=np.array([10,20,30,40,50])
print(arr[0:4])    
print(arr[3])    


# In[3]:


import numpy as np
a1=np.array([[1,2],[3,4]])
a2=np.array([[5,6],[7,8]])
b=np.hstack((a1,a2))
print(b)


# In[4]:


import numpy as np
a1=np.array([[1,2],[3,4]])
a2=np.array([[5,6],[7,8]])
b=np.vstack((a1,a2))
print(b)


# In[5]:


import numpy as np
a1=np.array([[1,2],[3,4]])
a2=np.array([[5,6],[7,8]])
b=np.dstack((a1,a2))
print(b)


# In[14]:


import numpy as np
a=np.array([1 ,2, 3, 4, 5, 6,7])
r=np.array_split(a,4)
print(r)


# In[ ]:




