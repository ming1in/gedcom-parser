#!/usr/bin/env python
# coding: utf-8

# In[7]:


from Gedcom import Gedcom, Family, Individual
import pandas as pd
import sys, os
from datetime import datetime


# In[32]:


def us53(gedcomFile):
    gedcom = Gedcom(gedcomFile)
    shared_bdays = []
    for indi in gedcom.individuals:
        bday = datetime.strftime(indi.birth, "%d %b")
        others = list(filter(lambda s: s != indi, gedcom.individuals))
        st = set()
        for ppl in others:
            if datetime.strftime(ppl.birth, "%d %b") == bday:
                st.add(ppl.name)
                st.add(indi.name)
                
        if st not in shared_bdays and len(st) > 0:
            shared_bdays.append(st)
    return shared_bdays
        

