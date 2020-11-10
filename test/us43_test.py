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
        result = ['I10', 'I14', 'I17']
        self.assertEqual(result, us43("seeds/testS31.ged"))

    def test2(self):
        result = ['I15', 'I16']
        self.assertEqual(result, us43("seeds/testS32.ged"))

    def test3(self):
        result = ['I17']
        self.assertEqual(result, us43("seeds/testS33.ged"))


if __name__ == '__main__':
    unittest.main()