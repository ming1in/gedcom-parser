'''
Created on 11/27/20
@author:   @arana23 - Aparajita Rana
Pledge:    I pledge my honor to abide by the Stevens Honor System
SSW555 - Sprint 4
'''

from Gedcom import Gedcom, Family, Individual
'''Goal: List family with most children'''

def us57(gedcomFile):
    gedcom = Gedcom(gedcomFile)
    maxFam = ''
    max = 0
    for fam in gedcom.families:
        count = 0
        for child in fam.child:
            count+=1
        if count>max:
            maxFam= fam.uid
            max=count

    return maxFam