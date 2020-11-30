'''
Created on 11/30/20
@author:   Susmitha Shailesh
Pledge:    I pledge my honor to abide by the Stevens Honor System.
SSW555 - Sprint 4

List names (first and last) shared by multiple individuals
'''

from Gedcom import Gedcom

def makeReturnString(sharedNames):

	sharedNames.sort

	if(len(sharedNames) == 0):
		return "There are no shared names." 
	else: 
		ret = "The following names are shared by multiple individuals:"

		for i in sharedNames:
			ret = ret + " " + i + ","

		if(ret[len(ret)-1] == ","):
			ret = ret[0:len(ret)-1]

		return(ret)



def listSharedNames(gedcom_name):

	gedcom = Gedcom(gedcom_name)

	inds = gedcom.individuals

	names = {}
	sharedNames = []

	for ind in inds:
		if ind.name in names:
			sharedNames.append(ind.name)
		else:
			names[ind.name] = 1

	ret = makeReturnString(sharedNames)
	return(ret)

print(listSharedNames("../test/seeds/test561.ged"))
