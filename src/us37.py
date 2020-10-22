'''
Created on 10/11/20
@author:   @arana23 - Aparajita Rana
Pledge:    I pledge my honor to abide by the Stevens Honor System
SSW555 - Sprint 2
'''
'''Goal: List all living spouses and descendants of people in a GEDCOM file who died in the last 30 days'''
from us36 import last30days
from Gedcom import Gedcom, Family

def us37(gedcomFile):
    gedcom = Gedcom(gedcomFile)
    fam_collections=[]
    for fam in gedcom.families:
        #check if husband dead
        if last30days(fam.husband.death):
            if fam.wife.death=='':
                fam_collections.append(fam.wife.name)
            for c in fam.child:
                if c.death=='':
                    fam_collections.append(c.name)

         #check if wife dead
        if last30days(fam.wife.death):
            if fam.husband.death=='':
                fam_collections.append(fam.wife.name)
            for c in fam.child:
                if c.death=='':
                    fam_collections.append(c.name)
        
        #check if children dead
        check=False
        for c in fam.child:
            if last30days(c.death):
                if fam.husband.death=='':
                    fam_collections.append(fam.husband.name)
                if fam.wife.death=='':
                    fam_collections.append(fam.wife.name)
                check=True
            if check:
                for c in fam.child:
                    if c.death=='':
                        fam_collections.append(c.name)

    return fam_collections