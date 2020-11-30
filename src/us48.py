#!/usr/bin/env python
# coding: utf-8

# In[10]:


from Gedcom import Gedcom, Family, Individual
import pandas as pd
import sys, os


# In[95]:


def us48(gedcomFile, n):
    gedcom = Gedcom(gedcomFile)
    cousins = []
    for indi in gedcom.individuals:
        if indi.name == n:
            person = indi
        
    famC = person.isChildToFamId
    if famC == '':
        return cousins
    
    for fam in gedcom.families:
        if fam.uid == famC:
            origin = fam
    if origin.husband.isChildToFamId == '' and origin.wife.isChildToFamId == '':
        return cousins
    
    parents = [origin.husband.isChildToFamId, origin.wife.isChildToFamId]
    parents = list(filter(lambda s: s != '', parents))
    aunts_uncles = [s for s in gedcom.individuals if s.isChildToFamId in parents and s.isChildToFamId != '']
    for rel in aunts_uncles:
        if rel.uid == origin.wife.uid or rel.uid == origin.husband.uid:
            aunts_uncles.remove(rel)
    for rel in aunts_uncles:
        for fam in gedcom.families:
            if fam.husband == rel or fam.wife == rel:
                for c in fam.child:
                    cousins.append(c.name)
        
    return cousins

