'''
Created on 11/9/20
@author:   Susmitha Shailesh
Pledge:    I pledge my honor to abide by the Stevens Honor System.
SSW555 - Sprint 3

List all couples who were married when the older spouse was more than twice as old as the younger spouse.
'''

from Gedcom import Gedcom
from datetime import date, datetime

def makeReturnString(largeDiff):

	largeDiff.sort

	if(len(largeDiff) == 0):
		return "No large age differences between spouses." 
	else: 
		ret = "The following couples have a large age difference:"

		for i in largeDiff:
			ret = ret + " " + i + ","

		if(ret[len(ret)-1] == ","):
			ret = ret[0:len(ret)-1]

		return(ret)

def calculateAge(birthDate, weddingDate): 
	age = weddingDate.year - birthDate.year - ((weddingDate.month, weddingDate.day) < (birthDate.month, birthDate.day)) 
	return age

def isAgeDiffLarge(husb_age, wif_age):
	if(husb_age > wif_age*2 or wif_age > husb_age*2):
		return True
	else:
		return False

def listLargeAgeDifferences(gedcom_name):

	gedcom = Gedcom(gedcom_name)

	inds = gedcom.individuals
	fams = gedcom.families

	largeDiff = []

	for fam in fams:
		if(fam.husband != '' and fam.wife != ''):
			husb = fam.husband
			husb_bday = husb.birth 
			husb_name = husb.name

			wif = fam.wife
			wif_bday = wif.birth
			wif_name = wif.name	

			wedding_date = fam.marriage

			if(husb_bday == '' or wif_bday == '' or wedding_date == ''):
				return("Not all dates are provided.")

			husb_wedding_age = calculateAge(husb_bday, wedding_date)
			wif_wedding_age = calculateAge(wif_bday, wedding_date)

			if(isAgeDiffLarge(husb_wedding_age, wif_wedding_age)):
				largeDiff.append(husb_name + " and " + wif_name)

	ret = makeReturnString(largeDiff)
	return(ret)
