'''
Created on 10/12/20
@author:   Susmitha Shailesh
Pledge:    I pledge my honor to abide by the Stevens Honor System.
SSW555 
This code has been refactored to eliminate bad smells.
'''

import pandas as pd
import Project02

'''
This function checks to see if there are any married siblings in the input .ged file
If there are no married siblings, the function returns True
If there are married siblings, the function returns a string of the individuals that violate the rule
'''
def siblingsShouldNotMarry(gedcom_name):
	df = Project02.createIndividualsDataFrame(gedcom_name) #get family database
	fam_dict = createFamDict(df) #parse family database
	error_string = findSiblingMarriages(fam_dict) #parse individuals
	
	if(error_string == ""):
		return True #no sibling marriages
	else: 
		to_return = formatErrorString(error_string) #sibling marriages
		return(to_return)

def createFamDict(df):
#creates dictionary that stores with families each individual is a part of

	fam_dict = {}
	
	for index, row in df.iterrows(): #iterates through dataframe
		fam_dict[row['Name']] = list([row['Child'],row['Spouse']]) #stores every Child, Spouse combination in fam_dict
	
	return fam_dict

def findSiblingMarriages(fam_dict):
#loops through fam_dict and find individuals who are marrying their siblings
	
	error_arr = []
	
	for entry in fam_dict:
		for secondEntry in fam_dict:
			#loops through every pair in fam_dict
			if entry == secondEntry: #same individual
				continue
			elif fam_dict[entry][0] == fam_dict[secondEntry][0] and fam_dict[entry][1] == fam_dict[secondEntry][1]: 
				#checks if any two individuals have the same child ID and family ID pair, indicating a sibling marriage
				error_arr.append(entry) #constructs array of all individuals in sibling marriages
	
	return error_arr

def formatErrorString(error_arr):
#formats error string in the correct way to be returned

	error_arr.sort()

	error_string = ""

	for i in error_arr:
		error_string = error_string + " " + entry + "," #constructs string of all individuals in sibling marriages
	
	if(error_string[len(error_string)-1] == ","):
		error_string = error_string[0:len(error_string)-1]
	s = "The following individuals are marrying their siblings, which is not allowed:" + error_string
	return s

