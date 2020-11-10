'''
Created on 10/24/20
@author:   Michael McCreesh
Pledge:    I pledge my honor to abide by the Stevens Honor System
SSW555 - Sprint 3
'''

'''Goal: Make sure there are no more than 5 births at a time'''
from Gedcom import Gedcom, Family

def us14(gedcomFile):
    gedcom = Gedcom(gedcomFile)
    badFams = []
    for fam in gedcom.families:
        count  = 0
        for child in fam.child:
            for kid in fam.child:
                if(child.birth == kid.birth):
                    count = count + 1
            if count > 5:
                badFams.append(fam)

    return badFams