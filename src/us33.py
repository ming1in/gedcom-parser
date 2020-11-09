'''
Created on 10/30/20
@author:   @arana23 - Aparajita Rana
Pledge:    I pledge my honor to abide by the Stevens Honor System
SSW555 - Sprint 3
'''

'''Goal: List all orphaned children (both parents dead and child < 18 years old) in a GEDCOM file'''
from Gedcom import Gedcom, Family

def us33(gedcomFile):
    gedcom = Gedcom(gedcomFile)
    orphan_collection=[]
    for fam in gedcom.families:
        if not fam.wife.death=='' and not fam.husband.death=='':
            for c in fam.child:
                if c.birth.year>2002:
                    orphan_collection.append(c.name)
    return orphan_collection