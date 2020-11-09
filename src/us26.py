'''
Created on 11/02/20
@author:   @arana23 - Aparajita Rana
Pledge:    I pledge my honor to abide by the Stevens Honor System
SSW555 - Sprint 3
'''

'''Goal: All family roles (spouse, child) specified in an individual record should have corresponding entries 
in the corresponding family records. Likewise, all individual roles (spouse, child) specified in family 
records should have corresponding entries in the corresponding  individual's records.  I.e. the information 
in the individual and family records should be consistent.'''

from Gedcom import Gedcom, Family, Individual

# Did a lot of creative choice w/ this function since the goal seemed vague
def us26(gedcomFile):
    gedcom = Gedcom(gedcomFile)
    fam_roles=[]
    fam_error=[]
    check=False
    #iterate through all individuals and collect all family references 
    for ind in gedcom.individuals:
        #if they have a family roles and we haven't accounted for that family yet -> add them to our list
        if(ind.isChildToFamId!='' and not fam_roles.__contains__(ind.isChildToFamId)):
            fam_roles+=[ind.isChildToFamId]
        elif(ind.isSpouseToFamId!='' and not fam_roles.__contains__(ind.isSpouseToFamId)):
            fam_roles+=[ind.isSpouseToFamId]
    
    #check if all of our different ids of families are in families correctly
    for id in fam_roles:
        for fam in gedcom.families:
            if(fam.uid==id):
                # we've hit the corresponding entry
                check=True
        #never hit the corresponding entry -> add to error fam list
        if(not check):
            fam_error+=[fam.uid]
        check=False
    #returns family ID's of error
    return fam_error