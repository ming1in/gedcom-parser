'''
Created on 11/30/20
@author:   Susmitha Shailesh
Pledge:    I pledge my honor to abide by the Stevens Honor System.
SSW555 - Sprint 4
'''

from Gedcom import Gedcom

def makeReturnString(living):

	living.sort

	if(len(living) == 0):
		return "There are no living individuals." 
	else: 
		ret = "The following individuals are living:"

		for i in living:
			ret = ret + " " + i + ","

		if(ret[len(ret)-1] == ","):
			ret = ret[0:len(ret)-1]

		return(ret)



def listLiving(gedcom_name):

	gedcom = Gedcom(gedcom_name)

	inds = gedcom.individuals

	living = []

	for ind in inds:
		if ind.death == "":
			living.append(ind.name)

	ret = makeReturnString(living)
	return(ret)
