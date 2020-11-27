import unittest
import sys
import os
sys.path.append(os.path.abspath('../src'))
from us33 import us33

class us33_test(unittest.TestCase):
    def test1(self):
      result = ['Dylan Smith','Evan Smith']
      self.assertEqual(result, us33("seeds/us33/test1.ged"))
    
    def test2(self):
      result = ['Susan Jones', 'Kevin Brown']
      self.assertEqual(result, us33("seeds/us33/test2.ged"))

if __name__ == '__main__':
    unittest.main()