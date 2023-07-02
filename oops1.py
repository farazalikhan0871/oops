#!/usr/bin/env python
# coding: utf-8

# INHERITANCE

# In[3]:


class parent:
    def method(self):
        
        return "this is created by faraz ali khan "


# In[6]:


class child(parent):
    def m1(self):
        return "i am learning python"


# In[7]:


obj = child()


# In[9]:


obj.m1()


# In[10]:


obj.method()


# In[ ]:





# MULTILABEL INHERITANCE 

# In[40]:


class t1():
    
    def m1(self):
        return "i a learning python"

class t2(t1): 
    
    def m2(self):
        return "i am learning aws cloud computing"
    
class t3(t2):
    def m3(self):
        return " i am a good full stack developer "


# In[29]:


obj = t3()
obj1 = t2()


# In[30]:


obj.m1()


# MULTIPLE INHERITANCE 

# In[31]:


class f1:
    def m1(self):
        return "my self faraz ali khan " 


# In[32]:


class f2:
    def m2(self):
        return " i am a little bit good boy"


# In[33]:


class f3:
    def m3(self):
        return "i will try to give my best always"


# In[34]:


class f4(f1,f2,f3):
    pass 


# In[36]:


obj = f4()


# In[37]:


obj.m1()


# ABSTRACTION ==> IT IS NOTHING BUT THE SKELETON OF SOMETHINIG

# In[44]:


import abc 
class bkit:
    
    @abc.abstractmethod
    def student_details(self):
        pass
    
    @abc.abstractmethod
    def student_marks(self):
        pass
    
    @abc.abstractmethod
    def student_attendance(self):
        pass 
    
    @abc.abstractmethod
    def student_semester(self):
        pass


# In[52]:


class cse(bkit):
    
    def student_attendance(self):
        return "this students is having very poor attendance "
    
    def student_details(self):
        " this students is having very good marks performance"


# In[53]:


class aiml(bkit):
    
    def student_attendance(self):
        return " this students us having very poor attendance "
    
    def student_details(self):
        return " this students is having very very good marks in the cld as well as the university "


# In[54]:


cse = cse()


# In[55]:


aiml = aiml()


# In[56]:


cse.student_marks()


# In[57]:


cse.student_attendance()


# In[ ]:




