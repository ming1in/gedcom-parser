# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 11:23:41 2020

@author: ptrda
"""

import unittest
import sys
import os
sys.path.append(os.path.abspath('../src'))
from us48 import us48


class us48_test(unittest.TestCase):
    def test1(self):
        result = ['James Jones', 'Michelle Jones']
        self.assertEqual(result, us48("seeds/us48/seed.ged", 'Evan Smith'))

    def test2(self):
        result = ['Dylan Smith', 'Evan Smith', 'Matthew Smith']
        self.assertEqual(result, us48("seeds/us48/seed.ged", 'Michelle Jones'))

    def test3(self):
        result = []
        self.assertEqual(result, us48("seeds/us48/seed.ged", 'Paul Smith'))


if __name__ == '__main__':
    unittest.main()
