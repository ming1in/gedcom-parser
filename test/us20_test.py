# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 20:19:50 2020

@author: ptrda
"""

import unittest
import sys
import os
sys.path.append(os.path.abspath('../src'))
from us20 import us20


class us35_test(unittest.TestCase):
    def test1(self):
        result = ['F4']
        self.assertEqual(result, us20("seeds/us20/testS31.ged"))

    def test2(self):
        result = ['F7']
        self.assertEqual(result, us20("seeds/us20/testS32.ged"))

    def test3(self):
        result = ['F4', 'F7']
        self.assertEqual(result, us20("seeds/us20/testS33.ged"))


if __name__ == '__main__':
    unittest.main()