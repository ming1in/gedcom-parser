#!/usr/bin/env python
# coding: utf-8

# Peter Damianov
# I pledge my Honor that I have abided by the Stevens Honor System

# In[1]:


import os
import sys
sys.path.append(os.path.abspath('../src'))



# In[5]:


from us22 import us22
import Project02


# In[6]:


import unittest


# In[7]:
# Checks if families returns false followed by checking if individuals returns false, hence [False, False]


class us22_test(unittest.TestCase):
    def test1(self):
        res = [False, False]
        self.assertEqual(us22('seed.ged'), res)
        
    def test2(self):
        res = [False, False]
        self.assertEqual(us22('test1.ged'), res)
    
    def test3(self):
        res = [False, False]
        self.assertEqual(us22('test2.ged'), res)
        
    def test4(self):
        res = [False, False]
        self.assertEqual(us22('test3.ged'), res)
        
    def test5(self):
        res = [False, False]
        self.assertEqual(us22('test5.ged'), res)

unittest.main(argv=['first-arg-is-ignored'], exit=False)


# In[ ]:




