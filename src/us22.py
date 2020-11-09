#!/usr/bin/env python
# coding: utf-8

# Peter Damianov
# I pledge my Honor that I have abided by the Stevens Honor System

# In[1]:


import os


# In[2]:


import sys


# In[4]:


import pandas as pd


# In[5]:


import Project02


# In[7]:


def us22(gedcom_file):
    families = Project02.createFamiliesDataFrame(gedcom_file)
    individuals = Project02.createIndividualsDataFrame(gedcom_file)
    
    dfs = [list(families.ID), list(individuals.ID)] 
    
    return (list(map(lambda lst: len(lst) != len(set(lst)), dfs)))
            

if __name__ == '__main__':
    invalid = us22('seed.ged')
    print(invalid)
# In[ ]:




