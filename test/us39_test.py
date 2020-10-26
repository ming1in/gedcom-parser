# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 00:09:06 2020

@author: ptrda
"""

import unittest
import sys
import os
sys.path.append(os.path.abspath('../src'))
from us39 import us39

class us39_test(unittest.TestCase):
    def test1(self):
      result = ['F1']
      self.assertEqual(result, us39("seeds/us39/testA.ged"))

    def test2(self):
      result = ['F1', 'F2']
      self.assertEqual(result, us39("seeds/us39/testB.ged"))

    def test3(self):
      result = []
      self.assertEqual(result, us39("seeds/us39/testC.ged"))

if __name__ == '__main__':
    unittest.main()