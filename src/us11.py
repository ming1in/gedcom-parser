'''
Author: Grace Miguel
I pledge my honor that I've abided by the Stevens Honor System
'''
import os 
import sys
import copy
from Gedcom import Gedcom, Family
os.chdir(os.path.abspath('test/seeds'))
#no bigamy aka no polyamorous relationships

def us11(gedcom_file):
    gedcom = Gedcom(gedcom_file)
    #creating empty lists of husbands and wives to then use as keys for dictionaries to check for multiple partners
    hubby = []
    wifey = []
    for x in gedcom.families:
       hubby.append(x.husband)
    
    for y in gedcom.families:
        wifey.append(y.wife)
    hub_marr = dict.fromkeys(hubby, 0)      #intalizing empty dict of husbands
    wife_marr = dict.fromkeys(wifey, 0)     #initalizing empty dict of wives
   
    for fam in gedcom.families: 
        if fam.marriage and not fam.divorce:        #check to see if there's a marriage & no divorce
            if fam.husband:
                hub_marr[fam.husband] += 1          #add 1 for each relationship
            if fam.wife:
                wife_marr[fam.wife] += 1
    for key in hub_marr.keys():
        if hub_marr[key]>1:
            return "There is a polyamorous relationship"
    for key in wife_marr.keys():
        if wife_marr[key]>1:
            return  "There is a polyamorous relationship"

