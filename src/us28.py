'''
Created on 10/24/20
@author:   Michael McCreesh
Pledge:    I pledge my honor to abide by the Stevens Honor System
SSW555 - Sprint 2
'''

'''Goal: List siblings in age order'''

from Gedcom import Gedcom, Family
from datetime import date, datetime

def sibList(fam):
    kidList = fam.child
    
    n = len(kidList) 
    for i in range(n-1): 
        for j in range(0, n-i-1): 
            day1 =kidList[j].birth
            day2 = kidList[j+1].birth
            if day1 < day2 : 
                kidList[j], kidList[j+1] = kidList[j+1], kidList[j]
    order = []
    for kid in kidList:
        order.append(kid.uid)
    return order


def us28(gedcomFile):
    gedcom = Gedcom(gedcomFile)
    fams = []
    for fam in gedcom.families:
        fams.append(sibList(fam))
    return fams

print(us28("../test/seeds/test6.ged"))