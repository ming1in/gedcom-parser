'''
Created on 09/27/20
@author:   Susmitha Shailesh
Pledge:    I pledge my honor to abide by the Stevens Honor System.
SSW555 - Sprint 1
'''

import unittest
import sys
import os 
sys.path.append(os.path.abspath('../src'))
import us18

class us18_test(unittest.TestCase):

    '''gedcom file with one sibling marriage'''
    def test1(self):
        s = "The following individuals are marrying their siblings, which is not allowed: Alexa Smith, Sam Smith"
        self.assertEqual(s, us18.siblingsShouldNotMarry("seeds/test181.ged"))

    '''gedcom file with three sibling marriages'''
    
    def test2(self):
        s = "The following individuals are marrying their siblings, which is not allowed: Claire Smith, Cody Smith, James Smith, Jen Smith, Rachel Smith, Rick Smith"
        self.assertEqual(s, us18.siblingsShouldNotMarry("seeds/test182.ged"))

    '''gedcom file with no sibling marriages'''
    def test3(self):
        self.assertTrue(us18.siblingsShouldNotMarry("seeds/test183.ged"))

    '''larger gedcom file with no sibling marriages'''
    def test4(self):
        self.assertTrue(us18.siblingsShouldNotMarry("seeds/test184.ged"))

    '''gedcom file with no sibling marriages, 
        but an individual is married to someone with the same name as their sibling '''
    def test5(self):
        self.assertTrue(us18.siblingsShouldNotMarry("seeds/test185.ged"))


if __name__ == '__main__':
    unittest.main()