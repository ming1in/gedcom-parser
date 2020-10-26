'''
Created on 10/24/20
@author:   Michael McCreesh
Pledge:    I pledge my honor to abide by the Stevens Honor System
SSW555 - Sprint 2
'''

'''Goal: Make sure there are no more than 15 siblings per family'''

from Gedcom import Gedcom, Family

def us15(gedcomFile):
    gedcom = Gedcom(gedcomFile)
    badFams = []
    for fam in gedcom.families:
        if len(fam.child) > 15 :
            badFams.append(fam.uid)
    return badFams
