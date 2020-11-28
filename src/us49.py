'''
Author: Grace Miguel
Date: 11/27/2020
I pledge my honor that I've abided by the Stevens Honor Code.
'''
import sys
import os
#from Gedcom import Gedcom, Family
from Gedcom import Gedcom, Family 
#This function lists families with only daughters
def us49(gedcom_file):
    children = []
    gedcom = Gedcom(gedcom_file)
    families = gedcom.families
    x = 0
    for fam in families:
        for children in fam.child:
            if children.sex == 'M':
                x +=1
        if x == 0:
            return(i.uid + " " + i.husband.name + " "+ i.wife.name ) 
        x=0
    
    
        
        
   