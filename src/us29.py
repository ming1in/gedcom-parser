'''
@author: Ming Lin

User Story #29: List deceased

List all deceased individuals in a GEDCOM file
'''

from Gedcom import Gedcom


def us29(gedcomFile):
    gedcom = Gedcom(gedcomFile)

    deadIndividuals = []

    for individual in gedcom.individuals:
        if (individual.death != ''):
            deadIndividuals.append(individual.uid)

    return deadIndividuals
