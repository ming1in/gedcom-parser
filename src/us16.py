'''
Created on 10/04/20
@author:   Susmitha Shailesh
Pledge:    I pledge my honor to abide by the Stevens Honor System.
SSW555 - Sprint 1
'''

import pandas as pd
import Project02

'''
This function checks to see if there are any married siblings in the input .ged file
If there are no married siblings, the function returns True
If there are married siblings, the function returns a string of the individuals that violate the rule
'''
def maleLastNames(gedcom_name):
	idf = Project02.createIndividualsDataFrame(gedcom_name)
	fdf = Project02.createFamiliesDataFrame(gedcom_name)

	lastNames = {}
	lastNamesCheck = {}
	error_string = "" 

	for index, row in fdf.iterrows(): #iterates through families dataframe
		#store last name of husband
		lastName = row['Husband Name'] 
		if(not(pd.isna(lastName))): #if there is a husband
			for i in lastName:
				if i != " ":
					lastName = lastName[1:]
				else:
					break
			lastName = lastName[1:]

			lastNames[row['ID']] = lastName #stores key=family ID value=lastName in dict
			lastNamesCheck[row['ID']] = True #stores key=family ID value=True in dict (later used to keep track of errors)


	for index, row in idf.iterrows(): #iterates through individuals dataframe
		if row['Gender'] == "M" and row['Child'] in lastNames.keys(): #if male
			#store last name of individual
			childLastName = row['Name'] 
			for i in childLastName:
				if i != " ":
					childLastName = childLastName[1:]
				else:
					break
			childLastName = childLastName[1:]

			if(childLastName != lastNames[row['Child']]): #checks if last names match, sets value to False in lastNamesCheck if not
				lastNamesCheck[row['Child']] = False

	#constructs error string
	#loops through lastNamesCheck, if value is False then there was an error in that family
	for i in lastNamesCheck:
		if(lastNamesCheck[i] == False):
			error_string = error_string + " " + i + ","


	if(error_string == ""):
		return True #males same last name
	else: 
		#males different last names
		if(error_string[len(error_string)-1] == ","):
			error_string = error_string[0:len(error_string)-1]
		s = "The following families have males that do not share the same last name, which is not allowed:" + error_string
		
		return s

