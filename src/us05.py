'''
Author: Grace Miguel
I pledge my honor that I've abided by the Stevens Honor Code.
'''
import sys
import copy
import os
import pandas as pd
from datetime import datetime
import Project02
os.chdir(os.path.abspath('../test/seeds'))
#checks to see if Marriage date is after death date
def us05(gedcom_file):
    individuals = Project02.createIndividualsDataFrame(gedcom_file)
    families = Project02.createFamiliesDataFrame(gedcom_file)
    fam = copy.deepcopy(families[['Husband Name','Wife Name', 'Married']])
    indivs = copy.deepcopy(individuals[[ 'Dead', 'Name']])
    error = []
    for i, row in fam.iterrows():           #iterates through both the fam and indivs
        for k, rows in indivs.iterrows():
            if row['Husband Name']==rows['Name']:        #checks if IDs are the same
                if type(row['Married']) == float and pd.isna(row['Married']):        #Checks to see if they're married
                    pass
                elif pd.to_datetime(row['Married']) > pd.to_datetime(rows['Dead']):  #Checks to see if the marriage date is after death
                    error.append(row['Husband Name'])
                    error.append(row["Wife Name"])
    if len(error)>0:
        print("The following people have marriage dates after death date: " + str(error))


