#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
x = np.arange(0,100)
y = x*2
z = x**2


# In[ ]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[5]:


figu = plt.figure()
axi = figu.add_axes([0,0,1,1])
axi.plot(x,y)
axi.set_xlabel('x')
axi.set_ylabel('y')
axi.set_title('title')


# In[6]:


fig = plt.figure()

axi1 = fig.add_axes([0,0,1,1])
axi2 = fig.add_axes([0.2,0.5,.2,.2])


# In[9]:


axi1.plot(x,y)
axi1.set_xlabel('x')
axi1.set_ylabel('y')


axi2.plot(x,y)
axi2.set_xlabel('x')
axi2.set_ylabel('y')
fig


# In[10]:


fig = plt.figure()

axi = fig.add_axes([0,0,1,1])
axi2 = fig.add_axes([0.2,0.5,.4,.4])


# In[11]:


axi.plot(x,z)
axi.set_xlabel('X')
axi.set_ylabel('Z')


axi2.plot(x,y)
axi2.set_xlabel('X')
axi2.set_ylabel('Y')
axi2.set_title('zoom')
axi2.set_xlim(20,22)
axi2.set_ylim(30,50)
fig


# In[12]:


fig, axes = plt.subplots(nrows=1, ncols=2)


# In[15]:


axes[0].plot(x,y,color="blue", lw=3, ls='--')
axes[1].plot(x,z,color="red", lw=3, ls='-')
fig


# In[16]:


fig, axes = plt.subplots(nrows=1, ncols=2,figsize=(12,2))

axes[0].plot(x,y,color="blue", lw=5)
axes[0].set_xlabel('x')
axes[0].set_ylabel('y')

axes[1].plot(x,z,color="red", lw=3, ls='--')
axes[1].set_xlabel('x')
axes[1].set_ylabel('z')

