'''
@author: Ming Lin

User Story #47: List widows

List all widows and widowers
'''
from Gedcom import Gedcom


def us47(gedcomFile):
    gedcom = Gedcom(gedcomFile)
    widows = []

    for family in gedcom.families:

        if (family.wife.death and not family.husband.death):
          if(family.husband.uid not in widows):
            widows.append(family.husband.uid)
        elif (family.husband.death and not family.wife.death):
          if(family.wife.uid not in widows):
            widows.append(family.wife.uid)

    return widows
