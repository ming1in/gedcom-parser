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
import us56

class us56_test(unittest.TestCase):

    def test1(self):
        s = "There are no shared names."
        self.assertEqual(s, us56.listSharedNames("seeds/seed.ged"))

    def test2(self):
        s = "The following names are shared by multiple individuals: John Johnson, Katie Jacobs"
        self.assertEqual(s, us56.listSharedNames("seeds/test561.ged"))


if __name__ == '__main__':
    unittest.main()