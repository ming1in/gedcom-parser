#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Gedcom import Gedcom, Individual
import pandas as pd


# In[29]:


def us43(gedcomFile):
    gedcom = Gedcom(gedcomFile)
    birthdays = []
    for indi in gedcom.individuals:
        birthdays.append((indi.birth, indi))
    twins = []
    for indi in gedcom.individuals:
        days = birthdays
        days.remove((indi.birth, indi))
        for date in days:
            if indi.birth == date[0]:
                if indi.isChildToFamId == date[1].isChildToFamId:
                    twins.append((indi.name, date[1].name))
    
    return twins

