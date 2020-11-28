# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 20:27:17 2020

@author: ptrda
"""

import unittest
import sys
import os
sys.path.append(os.path.abspath('../src'))
from us43 import us43


class us35_test(unittest.TestCase):
    def test1(self):
        result = [('Paul Smith', 'Peter Smith'),
                  ('Evan Smith', 'Matthew Smith'),
                  ('Mark Jones', 'Michelle Jones')]
        self.assertEqual(result, us43("seeds/us43/testS31.ged"))

    def test2(self):
        result = [('Macy MIGUEL', 'KATHERINE MIGUEL')]
        self.assertEqual(result, us43("seeds/us43/testS32.ged"))

    def test3(self):
        result = [('Sara Jones', 'Susan Jones')]
        self.assertEqual(result, us43("seeds/us43/testS33.ged"))


if __name__ == '__main__':
    unittest.main()