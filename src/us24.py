'''
@author: Ming Lin

User Story #25: Unique families by spouses

No more than one family with the same spouses by name 
and the same marriage date should appear in a GEDCOM file
'''

from Gedcom import Gedcom, Family
import sys
import os

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

      primaryHusband = list(filter(lambda individual: individual.uid == primaryFamily.husband, gedcom.individuals))[0]
      primaryWife = list(filter(lambda individual: individual.uid == primaryFamily.wife, gedcom.individuals))[0]
      
      for j, secondaryFamily in enumerate(gedcom.families):
        if (primaryFamily.uid == secondaryFamily.uid or not validFamily(secondaryFamily)):
          continue

        secondaryHusband = list(filter(lambda individual: individual.uid == secondaryFamily.husband, gedcom.individuals))[0]
        secondaryWife = list(filter(lambda individual: individual.uid == secondaryFamily.wife, gedcom.individuals))[0]
        
        if (primaryHusband.name == secondaryHusband.name and primaryWife.name == secondaryWife.name and primaryFamily.marriage == secondaryFamily.marriage):
          deletedFamilyIds.append(secondaryFamily.uid)

          gedcom.deleteFamily(secondaryFamily)
          
  return deletedFamilyIds
  

