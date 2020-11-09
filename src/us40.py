'''
Author: Grace Miguel
I pledge my honor that I've abided by the Stevens Honor Code 

US 40
'''

import sys
import os 
os.chdir(os.path.abspath('test/seeds'))

#prints line numbers of Gedcom File
def us40(gedcom_file):
    with open(gedcom_file, 'r') as f:
        for i, line in enumerate(f, start=0):
            return ('{} = {}'.format(i, line.strip()))
    
