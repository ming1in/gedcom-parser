import unittest
import sys
import os
sys.path.append(os.path.abspath('../src'))
from us57 import us57
from Gedcom import Gedcom, Family

class us57_test(unittest.TestCase):
    def test1(self):
      result = 'F2'
      self.assertEqual(result, us57("seeds/test1.ged"))

    def test2(self):
      result = 'F2'
      self.assertEqual(result, us57("seeds/test3.ged"))

if __name__ == '__main__':
    unittest.main()