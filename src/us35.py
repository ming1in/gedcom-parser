'''
@author: Ming Lin

User Story #35: List recent births

List all people in a GEDCOM file who were 
born in the last 30 days
'''
from Gedcom import Gedcom, Family
from datetime import date, datetime, timedelta
from us36 import last30days

def us35(gedcomFile):
  gedcom = Gedcom(gedcomFile)
  bornLast30Days = []

  for individual in gedcom.individuals:
     if last30days(individual.birth):
       bornLast30Days.append(individual.uid)

  return bornLast30Days
