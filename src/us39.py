#!/usr/bin/env python
# coding: utf-8

# In[6]:


from Gedcom import Gedcom
from datetime import datetime

# In[ ]:


from us38 import upcomingDate


# In[60]:


def us39 (gedcom_file):
    
    gedcom = Gedcom(gedcom_file)
    
    upcomingAnn = [family.uid for family in gedcom.families 
                     if (family.marriage != '' and upcomingDate(datetime.strftime(family.marriage, "%d %b")))]
    
    return upcomingAnn
