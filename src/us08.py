'''
@author: Ming Lin

User Story #08: Birth before marriage of parents

Children should be born after marriage of parents
(and not more than 9 months after their divorce)
'''
from Gedcom import Gedcom, Family
from datetime import datetime


def us08(gedcomFile):
    gedcom = Gedcom(gedcomFile)

    removedChildren = []

    for family in gedcom.families:
        if(len(family.child) > 0):
            if (family.marriage):

                remove = []
                for child in family.child:
                    if family.marriage and family.marriage > child.birth:
                        remove.append(child)
                        removedChildren.append(child.uid)
                    if (family.divorce and (child.birth - family.divorce).days > 90):
                        remove.append(child)
                        removedChildren.append(child.uid)
                if (len(remove) > 0):
                    for child in remove:
                        family.child.remove(child)

    return removedChildren
