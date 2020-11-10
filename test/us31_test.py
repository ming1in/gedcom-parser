'''
Created on 10/26/20
@author:   Susmitha Shailesh
Pledge:    I pledge my honor to abide by the Stevens Honor System.
SSW555 - Sprint 2
'''

import unittest
import sys
import os 
sys.path.append(os.path.abspath('../src'))
import us31

class us31_test(unittest.TestCase):

    def test1(self):
        s = "The following individuals are living and single: Paul Smith, James Jones, Michelle Jones, Evan Smith, Matthew Smith, Dylan Smith"
        self.assertEqual(s, us31.listLivingSingle("seeds/seed.ged"))

    def test2(self):
        s = "The following individuals are living and single: Patrick Smith"
        self.assertEqual(s, us31.listLivingSingle("seeds/test181.ged"))

    def test3(self):
        s = "There are no living single individuals."
        self.assertEqual(s, us31.listLivingSingle("seeds/test311.ged"))


if __name__ == '__main__':
    unittest.main()