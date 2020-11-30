'''
Author: Grace Miguel
Date: 11/27/20
I pledge my honor that I've abided by the Stevens Honor System
'''
#function prints the families with only sons
from Gedcom import Gedcom,Family 
import sys
import os
def us50(gedcom_file):
    gedcom = Gedcom(gedcom_file)
    families = gedcom.families
    x = 0
    for fam in families:
        for children in fam.child:
            if children.sex =='F':
                x +=1
        if x == 0:
            fams = []
            fams.append(fam.uid + " " + fam.husband.name + " "+ fam.wife.name)
        x=0
    return fams

