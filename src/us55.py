'''
@author: Michael McCreesh

User Story #55: List Couples without children

List the family ID of all the couples that do not have any children
'''
from Gedcom import Gedcom, Family

def us55(gedcomFile):
    gedcom = Gedcom(gedcomFile)
    lst = []
    for fam in gedcom.families:
        if len(fam.child) == 0:
            lst.append(fam.uid)
    return lst