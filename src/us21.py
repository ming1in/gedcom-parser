'''
Created on 11/9/20
@author:   Susmitha Shailesh
Pledge:    I pledge my honor to abide by the Stevens Honor System.
SSW555 - Sprint 3

Husband in family should be male and wife in family should be female
'''

from Gedcom import Gedcom

def makeReturnString(wrongGender):

	wrongGender.sort

	if(len(wrongGender) == 0):
		return "All roles and genders match." 
	else: 
		ret = "The following individuals have genders that do not match their roles:"

		for i in wrongGender:
			ret = ret + " " + i + ","

		if(ret[len(ret)-1] == ","):
			ret = ret[0:len(ret)-1]

		return(ret)



def correctGenderForRoles(gedcom_name):

	gedcom = Gedcom(gedcom_name)

	inds = gedcom.individuals
	fams = gedcom.families

	wrongGender = []

	for fam in fams:
		if(fam.husband != ''):
			husb = fam.husband
			if husb.sex == 'F':
				wrongGender.append(husb.name)

		if(fam.wife != ''):
			wif = fam.wife
			if wif.sex == 'M':
				wrongGender.append(wif.name)


	ret = makeReturnString(wrongGender)
	return(ret)