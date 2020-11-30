'''
Created on 11/8/20
@author:   Susmitha Shailesh
Pledge:    I pledge my honor to abide by the Stevens Honor System.
SSW555 - Sprint 3
'''

import unittest
import sys
import os 
sys.path.append(os.path.abspath('../src'))
import us34

class us34_test(unittest.TestCase):

	def test1(self):
		s = "No large age differences between spouses."
		self.assertEqual(s, us34.listLargeAgeDifferences("seeds/seed.ged"))

	def test2(self):
		s = "The following couples have a large age difference: John Jones and Sarah Jones Smith"
		self.assertEqual(s, us34.listLargeAgeDifferences("seeds/test341.ged"))


if __name__ == '__main__':
    unittest.main()