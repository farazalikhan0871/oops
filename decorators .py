#!/usr/bin/env python
# coding: utf-8

# In[1]:


class faraz:
    
    def __init__(self,name, email):
        self.__name = name 
        self.__email= email
        
    def set_name(self,name):
        self.__name = name
        
    def get_name(self):
        print(self.__name)
        


# In[2]:


obj = faraz("faraz",'kk@gmail.com')


# In[3]:


obj._faraz__name


# In[10]:


obj.set_name('tabrez')


# In[11]:


obj.get_name()


# In[ ]:





# In[12]:


obj.set_name('arbaz')


# In[13]:


obj.__dict__


# 

# DECORATORS IN PYTHON
# 

# In[150]:


def dec(fun):
    
    def inner_dec():
        
        print('-------start of the python code------- ')
        fun()
        print("-------end of the python code------- ")
    
    return inner_dec()


# In[164]:


def f1():
    print("faraz ali khan \n"+"i am learning python")
    print("faraz ali khan \n","i am learning python")
    

    


# In[165]:


f1()


# In[166]:


@dec
def f1():
    print("faraz ali khan \n")
    
    

    


# In[167]:


f1()


# 

# KNOWING THE TIME COMPLEXITY OF THE PYTHON CODE

# In[122]:


import time


# In[142]:


def timmer_test(fun):
    def inner_timmer():
        start = time.time()
        fun()
        end = time.time()
        print(start-end)
    return inner_timmer


# In[143]:


@timmer_test
def fun1():
    print(33+22)


# In[144]:


fun1()


# In[ ]:





# In[ ]:





# In[ ]:




