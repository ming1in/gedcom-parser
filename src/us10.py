''' Author:     Samantha Inneo
    Sprint:     Sprint 2
    User Story: Marriage should be at least 14 years after birth of both spouses (parents must be at least 14 years old)
    '''
import datetime
import unittest
import copy
from datetime import date
import Project02
import pandas as pd

        
def marriedTooYoung(gedcom_name):
    individuals = Project02.createIndividualsDataFrame(gedcom_name)
    families = Project02.createFamiliesDataFrame(gedcom_name)
    fam = copy.deepcopy(families[['Husband ID','Wife ID', 'Married']])
    indivs = copy.deepcopy(individuals[[ 'Birthday', 'ID']])
    badHusbands = []
    badWives = []
    d0 = date(2014, 1, 1)
    d1 = date(2000, 1,1)
    delta = d0-d1
    fourteen_years = delta.days 
    for i, row in fam.iterrows():          
        for k, rows in indivs.iterrows():
            if row['Husband ID'] == rows['ID']: 
                if type(row['Married']) == float and pd.isna(row['Married']):        
                    pass
                elif (pd.to_datetime(row['Married']) - pd.to_datetime(rows['Birthday'])).days < fourteen_years :  
                    badHusbands.append(row['Husband ID'])
            if row['Wife ID'] == rows['ID']: 
                if type(row['Married']) == float and pd.isna(row['Married']):        
                    pass
                elif (pd.to_datetime(row['Married']) - pd.to_datetime(rows['Birthday'])).days < fourteen_years :  
                    badWives.append(row["Wife ID"])
    if len(badHusbands)>0 or len(badWives)>0:
        return("The following people have marriage before the age of 14: Husbands" + str(badHusbands) + " Wives: " + str(badWives))
    else:
        return("All marriages at acceptable age!")
   