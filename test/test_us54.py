import unittest
import sys
import os
sys.path.append(os.path.abspath('../src'))
from us54 import us54
from Gedcom import Gedcom, Family

class test_us54(unittest.TestCase):
    def test1(self):
      result = [['F1', 3], ['F2', 4], ['F3', 3]]
      self.assertEqual(result, us54("seeds/test1.ged"))

    def test2(self):
      result = [['F1', 4], ['F2', 4], ['F3', 4], ['F4', 3]]
      self.assertEqual(result, us54("seeds/test2.ged"))

    def test3(self):
      result = [['F1', 2], ['F2', 4]]
      self.assertEqual(result, us54("seeds/test3.ged"))

    def test4(self):
      result = [['F1', 4], ['F2', 4], ['F3', 4], ['F4', 3]]
      self.assertEqual(result, us54("seeds/test5.ged"))

    def test5(self):
      result = [['F1', 4], ['F2', 5], ['F3', 4], ['F4', 2], ['F5', 2], ['F6', 3]]
      self.assertEqual(result, us54("seeds/test6.ged"))

if __name__ == '__main__':
    unittest.main()