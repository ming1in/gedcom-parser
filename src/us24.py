'''
@author: Ming Lin

User Story #25: Unique families by spouses

No more than one family with the same spouses by name 
and the same marriage date should appear in a GEDCOM file
'''

from Gedcom import Gedcom, Family


def validFamily(family: Family):
    if (family.husband != '' and family.wife != '' and family.marriage != ''):
        return True
    else:
        return False


def us24(gedcomFile):
    gedcom = Gedcom(gedcomFile)
    deletedFamilyIds = []

    for idx, primaryFamily in enumerate(gedcom.families):
        if (validFamily(primaryFamily) and primaryFamily.uid not in deletedFamilyIds):

            for j, secondaryFamily in enumerate(gedcom.families):
                if (primaryFamily.uid == secondaryFamily.uid or not validFamily(secondaryFamily)):
                    continue

                if (primaryFamily.husband.name == secondaryFamily.husband.name and primaryFamily.wife.name == secondaryFamily.wife.name and primaryFamily.marriage == secondaryFamily.marriage):
                    deletedFamilyIds.append(secondaryFamily.uid)

                    gedcom.deleteFamily(secondaryFamily)

    return deletedFamilyIds
