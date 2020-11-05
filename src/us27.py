'''
Created on 10/25/20
@author:   Susmitha Shailesh
Pledge:    I pledge my honor to abide by the Stevens Honor System.
SSW555 - Sprint 2
'''

from Gedcom import Gedcom
from datetime import date, datetime

def makeReturnString(ages):

	ages.sort

	ret = ""

	for i in ages:
		ret = ret + " " + i

	ret = ret[1:]

	return(ret)

def calculateAge(birthDate): 
	today = date.today() 
	age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day)) 
	return age


def includeIndividualAges(gedcom_name):

	gedcom = Gedcom(gedcom_name)

	inds = gedcom.individuals

	ages = []

	for ind in inds:
		name = ind.name
		birthDate = datetime.strptime(ind.birth, '%d %b %Y')
		age = calculateAge(birthDate)
		ages.append(name + " is currently " + str(age) + " years old.")

	ret = makeReturnString(ages)
	print(ret)
	return(ret)

includeIndividualAges("../test/seeds/seed.ged")


