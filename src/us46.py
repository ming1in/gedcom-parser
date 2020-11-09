'''
Author:     Samantha Inneo
Sprint:     Sprint 3
Use Case:   List the IDs of only children
'''

import pandas as pd
import datetime
import copy
import os
from Gedcom import Gedcom, Family
from us28 import sibList




def us46(gedcom_name):
    gedcom = Gedcom(gedcom_name)
    onlyChildren = []
    for fam in gedcom.families:
        if(len(fam.child) == 1):
            onlyChildren.append(sibList(fam))
    if(len(onlyChildren) > 0):
        return onlyChildren
    else:
        return('No only children')
    
    
