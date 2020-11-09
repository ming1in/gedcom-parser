'''
Created on 10/25/20
@author:   Susmitha Shailesh
Pledge:    I pledge my honor to abide by the Stevens Honor System.
SSW555 - Sprint 2
'''

from Gedcom import Gedcom

def makeReturnString(livingSingle):

	livingSingle.sort

	if(len(livingSingle) == 0):
		return "There are no living single individuals." 
	else: 
		ret = "The following individuals are living and single:"

		for i in livingSingle:
			ret = ret + " " + i + ","

		if(ret[len(ret)-1] == ","):
			ret = ret[0:len(ret)-1]

		return(ret)



def listLivingSingle(gedcom_name):

	gedcom = Gedcom(gedcom_name)

	inds = gedcom.individuals

	livingSingle = []

	for ind in inds:
		if ind.isSpouseToFamId == "" and ind.death == "":
			livingSingle.append(ind.name)

	ret = makeReturnString(livingSingle)
	return(ret)