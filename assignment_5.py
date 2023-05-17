#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#1. What does an empty dictionary code look like?
ANS - empty dict = {}


# In[1]:


# 2. What is the value of a dictionary value with the key and the value 42?
ans = dict = {"foo":42}


# In[2]:


# 3. What is the most significant distinction between a dictionary and a list?
# ans = list is oreder and mutabal, dictionary is unordered and also mutable.
# list are used to store data and dict used to large amount of data easy for acces.


# In[3]:


# 4. What happens if you try to access spam[foo] if spam is {bar:100}?


# In[4]:


spam = {'bar':100}
spam['foo']


# 5. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.keys()?

# there is no difference

# In[8]:


spam = {'cat':5}
'cat' in spam


# In[9]:


'cat' in spam.keys()


# 6. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.values()?
# 

# 'cat' in spam.values() checks there is a value 'cat' for one of the keys in spam

# In[10]:


spam = {'cat':5}
'cat' in spam


# In[12]:


'cat' in spam.values()


# 7. What is a shortcut for the following code?

# if 'color' not in spam:
# spam['color'] = 'black'

# In[13]:


spam ={'cat':100}
spam.setdefault('color','black')


# In[14]:


spam


# 8. How do you 'pretty print' dictionary values using which module and function?

# In[15]:


import pprint


# In[16]:


dict = [ {'Name': 'yogi', 'Age': '23', 'Country': 'rusia'},
  {'Name': 'men', 'Age': '33', 'Country': 'uk'},
  {'Name': 'Anna', 'Age': '29', 'Country': 'japan'},
  {'Name': 'lio', 'Age': '31', 'Country': 'china'}
]


# In[17]:


print(dict)


# In[18]:


pprint.pprint(dict)


# In[ ]:




