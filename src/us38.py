#!/usr/bin/env python
# coding: utf-8

# In[6]:


from Gedcom import Gedcom


# In[7]:


from datetime import date, datetime, timedelta


# In[58]:


def upcomingDate (dt):
    
    if dt == '':
        return False
    
    today = datetime.today()
    upcomingDays = today + timedelta(days = 30)
    
    dt = datetime.strptime(dt + " " + date.today().strftime('%Y'), '%d %b %Y')
    
    
    return today <= dt <= upcomingDays


# In[60]:


def us38 (gedcom_file):
    
    gedcom = Gedcom(gedcom_file)
    
    upcomingBDays = [individual.name for individual in gedcom.individuals 
                     if (individual.birth != '' and upcomingDate(datetime.strftime(individual.birth, "%d %b")))]
    
    return upcomingBDays


