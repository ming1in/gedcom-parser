import unittest
import sys
import os
sys.path.append(os.path.abspath('../src'))
from us55 import us55
from Gedcom import Gedcom, Family

class test_us54(unittest.TestCase):
    def test1(self):
      result = []
      self.assertEqual(result, us55("seeds/test1.ged"))

    def test2(self):
      result = []
      self.assertEqual(result, us55("seeds/test2.ged"))

    def test3(self):
      result = ['F1']
      self.assertEqual(result, us55("seeds/test3.ged"))

    def test4(self):
      result = []
      self.assertEqual(result, us55("seeds/test5.ged"))

    def test5(self):
      result = ['F4', 'F5']
      self.assertEqual(result, us55("seeds/test6.ged"))

if __name__ == '__main__':
    unittest.main()