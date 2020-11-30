'''
Created on 11/27/20
@author:   @arana23 - Aparajita Rana
Pledge:    I pledge my honor to abide by the Stevens Honor System
SSW555 - Sprint 4
'''

from Gedcom import Gedcom, Family, Individual

'''Goal: List all couples(married) in family'''
def us52(gedcomFile):
    couples=[]

    gedcom = Gedcom(gedcomFile)
    for fam in gedcom.families:
        if fam.husband.name != None and fam.wife.name != None:
            couples.append(fam.husband.name)
            couples.append(fam.wife.name)
    
    return couples