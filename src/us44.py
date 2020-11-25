'''
Author:     Samantha Inneo
Sprint:     Sprint 4
Use Case:   Find the youngest person
'''

import pandas as pd
import datetime
import copy
import os
from Gedcom import Gedcom, Individual

def us44(gedcom_name):
    gedcom = Gedcom(gedcom_name)
    # if len(gedcom.individuals) == 0 :
    #     print("no members in this family")
    curr_youngest = gedcom.individuals[0]

    for indi in gedcom.individuals:
        if(indi.birth > curr_youngest.birth):
            curr_youngest = indi
    return curr_youngest.uid