'''
Created on 11/30/20
@author:   Susmitha Shailesh
Pledge:    I pledge my honor to abide by the Stevens Honor System.
SSW555 - Sprint 4
'''

import unittest
import sys
import os 
sys.path.append(os.path.abspath('../src'))
import us51

class us51_test(unittest.TestCase):

    def test1(self):
        s = "The following individuals are living: John Smith, Paul Smith, James Jones, Michelle Jones, Evan Smith, Matthew Smith, Susan Jones, Dylan Smith, Frank Jones, Emily Michaels, Bernard Smith, Theresa Kelly, Kevin Brown, Diane Brown"
        self.assertEqual(s, us51.listLiving("seeds/seed.ged"))

    def test2(self):
        s = "There are no living individuals."
        self.assertEqual(s, us51.listLiving("seeds/test511.ged"))


if __name__ == '__main__':
    unittest.main()