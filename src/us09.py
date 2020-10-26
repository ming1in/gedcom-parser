'''
@author: Ming Lin

User Story #09: Birth before death of parents

Child should be born before death of mother 
and before 9 months after death of father
'''
from Gedcom import Gedcom, Family
from datetime import datetime

def us09(gedcomFile):
  gedcom = Gedcom(gedcomFile)

  removedChildren =[]

  for family in gedcom.families:
    if (len(family.child) > 0):
      remove = []
      
      for child in family.child:
        if (family.wife.death and (child.birth > family.wife.death)):
          remove.append(child)
        if (family.husband.death and (child.birth - family.husband.death).days > 90):
          remove.append(child)
      
      if (len(remove) > 0):
          for child in remove:
            removedChildren.append(child.uid)
            family.child.remove(child)

  return removedChildren

          
