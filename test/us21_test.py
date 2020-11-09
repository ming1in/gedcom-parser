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
import us21

class us21_test(unittest.TestCase):

	def test1(self):
		s = "All roles and genders match."
		self.assertEqual(s, us21.correctGenderForRoles("seeds/seed.ged"))

	def test2(self):
		s = "The following individuals have genders that do not match their roles: Susan Jones, Bernard Smith, Theresa Kelly, Frank Jones, Kevin Brown, Kevin Brown"
		self.assertEqual(s, us21.correctGenderForRoles("seeds/test211.ged"))


if __name__ == '__main__':
    unittest.main()