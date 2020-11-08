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
import us27

class us27_test(unittest.TestCase):

    def test1(self):
        s = "John Smith is currently 55 years old. Paul Smith is currently 52 years old. James Jones is currently 13 years old. Lucia Johnson is currently 52 years old. Michelle Jones is currently 21 years old. Evan Smith is currently 22 years old. Matthew Smith is currently 24 years old. Susan Jones is currently 51 years old. Dylan Smith is currently 17 years old. Frank Jones is currently 80 years old. Emily Michaels is currently 78 years old. Bernard Smith is currently 80 years old. Theresa Kelly is currently 79 years old. Kevin Brown is currently 53 years old. Diane Brown is currently 50 years old."
        self.assertEqual(s, us27.includeIndividualAges("seeds/seed.ged"))

    def test2(self):
        s = "Casey Smith is currently 50 years old. John Jones is currently 50 years old. James Jones is currently 29 years old. Joana Jones is currently 20 years old. Pat Marcson is currently 1820 years old."
        self.assertEqual(s, us27.includeIndividualAges("seeds/test311.ged"))


if __name__ == '__main__':
    unittest.main()