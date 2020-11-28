'''
@author: Ming Lin

User Story #32: List multiple births

List all multiple births in a GEDCOM file
'''
from Gedcom import Gedcom


def us32(gedcomFile):
    gedcom = Gedcom(gedcomFile)
    births = {}
    multipleBirths = []

    for family in gedcom.families:
        if (len(family.child) > 0):
            # check is wife has given birth before in the case the wife has two families
            if family.wife.uid in births:
                births[family.wife.uid] += len(family.child)
            else:
                births[family.wife.uid] = len(family.child)

    # look in births dict for women with multiple births
    for uid in births:
        if births[uid] > 1:
            multipleBirths.append(uid)

    return multipleBirths
