'''
Author: Grace Miguel
I pledge my honor that I've abided by the Stevens Honor Code.
'''
import sys
import os
import copy
from datetime import datetime
import pandas as pd 
import Project02
os.chdir(os.path.abspath('../test/seeds'))
#This function is used to determine if the Divorce date is after the Death date
def us06(gedcom_file):
     individuals = Project02.createIndividualsDataFrame(gedcom_file)
     families = Project02.createFamiliesDataFrame(gedcom_file)
     indivs = copy.deepcopy(individuals[['Dead', 'Name']])
     fam = copy.deepcopy(families[['Husband Name', 'Wife Name', 'Divorced']])
     incorrect = []  
     for i, row in fam.iterrows():
         for k, rows in indivs.iterrows():
             if row['Wife Name']==rows['Name']:
                 if type(row['Divorced'])==float and pd.isna(row['Divorced']):
                     pass
                 elif pd.to_datetime(row['Divorced']) > pd.to_datetime(rows['Dead']):
                     incorrect.append(row["Wife Name"])
             if row['Husband Name']==rows['Name']:
                 if type(row['Divorced'])==float and pd.isna(row['Divorced']):
                     pass
                 elif pd.to_datetime(row['Divorced']) > pd.to_datetime(rows['Dead']):
                     incorrect.append(row["Husband Name"])
                    
     if len(incorrect)>0:
        print("The following people have divorces after their death date" + str(incorrect))

