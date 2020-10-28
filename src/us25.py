'''
@author: Ming Lin

User Story #25: Unique first names in families

No more than one child with the same name and 
birth date should appear in a family
'''
from Gedcom import Gedcom, Family


def us25(gedcomFile):
    gedcom = Gedcom(gedcomFile)
    removedChildren = []

    for idx, family in enumerate(gedcom.families):
        duplicateChildren = []

        if (len(family.child) <= 1):
            continue
        else:
            for idx, child in enumerate(family.child):
                duplicates = list(filter(lambda childList: childList.name == child.name and
                                         childList.birth == child.birth and
                                         childList.uid not in duplicateChildren and
                                         childList.uid != child.uid, family.child))

                if len(duplicates) > 0:
                    duplicateChildren.append(child.uid)

        if len(duplicateChildren) > 0:
            family.child = list(
                filter(lambda child: child.uid not in duplicateChildren, family.child))
            for child in duplicateChildren:
                removedChildren.append(child)

    return removedChildren
