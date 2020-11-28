#!/usr/bin/env python
# coding: utf-8

# In[17]:


from Gedcom import Gedcom, Family, Individual
import pandas as pd


# In[50]:


def us20 (gedcomFile):
    err = []
    gedcom = Gedcom(gedcomFile)
    for fam in gedcom.families:
        if fam.husband != '' and fam.wife != '':
        
            husbFam = fam.husband.isChildToFamId
            wifeFam = fam.wife.isChildToFamId
        
            for family in gedcom.families:
                if family.uid == husbFam:
                    husbParFam = family
                if family.uid == wifeFam:
                    wifeParFam = family
        
            husbParFam_husbFam = husbParFam.husband.isChildToFamId
            husbParFam_wifeFam = husbParFam.wife.isChildToFamId
            if (wifeFam != ''):
                if ((husbParFam_husbFam == wifeFam) or (husbParFam_wifeFam == wifeFam)):
                    err.append(fam.uid)
                    continue
        
            wifeParFam_husbFam = wifeParFam.husband.isChildToFamId
            wifeParFam_wifeFam = wifeParFam.wife.isChildToFamId
            if (husbFam != ''):
                if ((wifeParFam_husbFam == husbFam) or (wifeParFam_wifeFam == husbFam)):
                    err.append(fam.uid)
                    continue

    return err   