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
import us16

class us16_test(unittest.TestCase):

    
    def test1(self):
        s = "The following families have males that do not share the same last name, which is not allowed: F1"
        self.assertEqual(s, us16.maleLastNames("seeds/test161.ged"))

    
    def test2(self):
        s = "The following families have males that do not share the same last name, which is not allowed: F1, F2"
        self.assertEqual(s, us16.maleLastNames("seeds/test162.ged"))

    
    def test3(self):
        s = "The following families have males that do not share the same last name, which is not allowed: F1, F2, F3"
        self.assertEqual(s, us16.maleLastNames("seeds/test163.ged"))

    
    def test4(self):
        self.assertTrue(us16.maleLastNames("seeds/seed.ged"))


    def test5(self):
        self.assertTrue(us16.maleLastNames("seeds/test164.ged"))


if __name__ == '__main__':
    unittest.main()