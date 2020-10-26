'''
Author:     Samantha Inneo
Sprint:     Sprint 1
Use Case:   Birth dates of siblings should be more than 8 months apart or less than 2 days apart 
            (twins may be born one day apart, e.g. 11:59 PM and 12:02 AM the following calendar day)
'''

import pandas as pd
import datetime
import copy
import os
import Project02

def siblingsAgeGap(gedcom_name):
    # I need to gather all the siblings of each family
    # check if their birthdays are more than 8 months apart
    # check if their birthdays are less than 2 days apart
    #return true if they are valid, false if they are not
    # eight_months = 240
    # two_days = 2

    individuals = Project02.createIndividualsDataFrame(gedcom_name)
    families = Project02.createFamiliesDataFrame(gedcom_name)

    child = []
    #indiv = copy.deepcopy(individuals[["Name", "Birthday", "Dead"]])

    children = copy.deepcopy(families["Children"])
    # print(children)
    #for index, row in children.iterrows():
    invalids = 0
    for row in families.Children:
        #if there's more than one child
        if len(row) > 1:
            for i in range(len(row)):
                main = row[i]
                row2 = [n for n in row if n != main]
                
                main_d = pd.to_datetime(list(individuals[individuals.ID == main].Birthday)[0])
                for x in row2:
                    x_d = pd.to_datetime(list(individuals[individuals.ID == x].Birthday)[0])
                    if abs(int((main_d - x_d).days)) > 2:
                        if abs(int((main_d - x_d).days)) < 240:    
                            return("Individuals ", main, " and ", x, " are invalid.")
                            invalids+=1
    if invalids == 0:
        return("All siblings are valid")





       