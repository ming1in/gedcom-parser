'''
Created on 10/24/20
@author:   Michael McCreesh
Pledge:    I pledge my honor to abide by the Stevens Honor System
SSW555 - Sprint 3
'''

'''Goal: Make sure there are marriages between first cousins'''
from Gedcom import Gedcom, Family, Individual

def us19(gedcomFile):
    gedcom = Gedcom(gedcomFile)
    badFams = []
    for fam in gedcom.families:
        husbf = fam.husband.isChildToFamId
        wifef = fam.wife.isChildToFamId
        for family in gedcom.families:
            if family.uid == husbf:
                husbfam = family
            if family.uid == wifef:
                wifefam = family
        hdad = husbfam.husband
        hmom = husbfam.wife
        wdad = wifefam.husband
        wmom = wifefam.wife
        if hdad.isChildToFamId == wdad.isChildToFamId or hdad.isChildToFamId == wmom.isChildToFamId or hmom.isChildToFamId == wdad.isChildToFamId or hmom.isChildToFamId == wmom.isChildToFamId:
            badFams.append(fam)
    return badFams

def getAUFId(family, gedcom):
    mom = family.wife
    dad = family.husband
    for fam in gedcom.families:
        if(mom in fam.child):
            
