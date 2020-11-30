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
            fam = []
            fam.append(i.uid + " " + i.husband.name + " "+ i.wife.name)
        x=0
    for i in fam:
        return i

