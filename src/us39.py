#!/usr/bin/env python
# coding: utf-8

# In[6]:


from Gedcom import Gedcom
from datetime import datetime
import os

# In[ ]:


from us38 import upcomingDate


# In[60]:


def us39 (gedcom_file):
    
    gedcom = Gedcom(gedcom_file)
    
    upcomingAnn = [family.uid for family in gedcom.families 
                     if (family.marriage != '' and upcomingDate(datetime.strftime(datetime.strptime(family.marriage, "%d %b %Y"), "%d %b")))]
    
    return upcomingAnn

u = us39(os.path.abspath('../test/seeds/us39/testC.ged'))
print(u)