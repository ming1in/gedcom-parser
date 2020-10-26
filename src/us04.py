'''
Author:     Samantha Inneo
Sprint:     Sprint 2
Use Case:   Marriage should occur before divorce of spouses, and divorce can only occur after marriage
'''

import pandas as pd
import datetime
import copy
import os
import Project02

def marriageBeforeDivorce(gedcom_name):
    families = Project02.createFamiliesDataFrame(gedcom_name)
    fams = copy.deepcopy(families[['ID', 'Married', 'Divorced']])
    invalid_divorces = []
    printout = ""
    for i, row in fams.iterrows():
        if type(row['Divorced'])==float and pd.isna(row['Divorced']):
            continue
        elif pd.to_datetime(row['Divorced']) < pd.to_datetime(row['Married']):
            invalid_divorces.append(row['ID'])
    if(len(invalid_divorces) == 0):
        return("All marraiges ar valid.")
    elif(len (invalid_divorces) > 0):
        for i in invalid_divorces:
            printout += i + " is invalid."
        return printout
            
     

