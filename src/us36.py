'''
Created on 10/11/20
@author:   @arana23 - Aparajita Rana
Pledge:    I pledge my honor to abide by the Stevens Honor System
SSW555 - Sprint 2
'''

'''Goal: List all people in a GEDCOM file who died in the last 30 days'''

from Gedcom import Gedcom, Family
from datetime import date, datetime, timedelta

#SMELLY CODE FIX NO. 1: created seperate function for checking date
def last30days(date):
    if date=='':
        return False
    #SMELLY CODE FIX NO. 2: renamed variables so makes sense to reader
    today = datetime.today()
    older = today - timedelta(days=30)
    return older < date < today


def us36(gedcomFile):
    gedcom = Gedcom(gedcomFile)
    recentdeath=[]
    for indiv in gedcom.individuals:
        if last30days(indiv.death):
            recentdeath.append(indiv.name)
    return recentdeath
