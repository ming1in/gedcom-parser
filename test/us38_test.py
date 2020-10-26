# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 00:08:32 2020

@author: ptrda
"""

import unittest
import sys
import os
sys.path.append(os.path.abspath('../src'))
from us38 import us38

class us38_test(unittest.TestCase):
    def test1(self):
      result = ['Evan Smith', 'Dylan Smith']
      self.assertEqual(result, us38("seeds/us38/TestA.ged"))

    def test2(self):
      result = []
      self.assertEqual(result, us38("seeds/us38/TestB.ged"))

    def test3(self):
      result = ['LESLIE MIGUEL', 'VICTOR LAUCELLO']
      self.assertEqual(result, us38("seeds/us38/TestC.ged"))

if __name__ == '__main__':
    unittest.main()