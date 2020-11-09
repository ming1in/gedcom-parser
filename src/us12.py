'''
Author:     Samantha Inneo
Sprint:     Sprint 3
Use Case:   Checks if parents are too old to have children
'''

import pandas as pd
from datetime import date
import copy
import os
from Gedcom import Gedcom, Family
from us28 import sibList



# user stories with gedcom file: 8,9,15,24,25,28,29,35,36,37,38,39


def us12(gedcom_name):
    d0 = date(1980, 1, 1)
    d1 = date(1900, 1,1)
    d2 = date(1960,1,1)
    delta = d0-d1
    delta2 = d2-d1
    max_dad_age = delta.days 
    max_mom_age = delta2.days
    gedcom = Gedcom(gedcom_name)
    oldParents = []
    for family in gedcom.families:
        if (len(family.child) > 0):
        
            for child in family.child:
                if ((child.birth -family.wife.birth).days > max_mom_age):
                    if family.wife.uid in oldParents:
                        pass
                    else:
                        oldParents.append(family.wife.uid)
                if ((child.birth - family.husband.birth).days > max_dad_age):
                    if family.husband.uid in oldParents:
                        pass
                    else:
                        oldParents.append(family.husband.uid)            
    if(len(oldParents) > 0):
        return oldParents
    else:
        return "All parents are an acceptable age"