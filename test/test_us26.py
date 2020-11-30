import unittest
import sys
import os
sys.path.append(os.path.abspath('../src'))
from us26 import us26

class us26_test(unittest.TestCase):
    def test1(self):
      result = ['F6']
      self.assertEqual(result, us26("seeds/us26/test1.ged"))
    
    def test2(self):
      result = []
      self.assertEqual(result, us26("seeds/us26/test2.ged"))

if __name__ == '__main__':
    unittest.main()