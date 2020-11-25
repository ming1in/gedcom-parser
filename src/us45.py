'''
Author:     Samantha Inneo
Sprint:     Sprint 4
Use Case:   Find the oldest living person
'''

import pandas as pd
import datetime
import copy
import os
from Gedcom import Gedcom, Individual

def us45(gedcom_name):
    gedcom = Gedcom(gedcom_name)
    # if len(gedcom.individuals) == 0 :
    #     print("no members in this family")
    curr_oldest = gedcom.individuals[0]

    for indi in gedcom.individuals:
        if(indi.birth < curr_oldest.birth) and not(indi.death):
            curr_oldest = indi
    return curr_oldest.uid