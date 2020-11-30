'''
@author: Michael McCreesh

User Story #54: List umber of family memebers

List umber of family memebers in each different family
'''
from Gedcom import Gedcom, Family

def us54(gedcomFile):
    gedcom = Gedcom(gedcomFile)
    lst = []
    for fam in gedcom.families:
        mems = len(fam.child) + 2
        lst.append([fam.uid, mems])
    return lst