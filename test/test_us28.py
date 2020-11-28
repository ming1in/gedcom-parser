import unittest
import sys
import os
sys.path.append(os.path.abspath('../src'))
from us28 import us28

class us28_test(unittest.TestCase):
    def test1(self):
      result = [['I5'], ['I4', 'I1'], ['I3']]
      self.assertEqual(result, us28("seeds/test1.ged"))

    def test2(self):
      result = [['I3', 'I4'], ['I5', 'I6'], ['I7', 'I8'], ['I9']]
      self.assertEqual(result, us28("seeds/test2.ged"))

    def test3(self):
      result = [[], ['I4', 'I1']]
      self.assertEqual(result, us28("seeds/test3.ged"))

    def test4(self):
      result = [['I3', 'I4'], ['I5', 'I6'], ['I7', 'I8'], ['I9']]
      self.assertEqual(result, us28("seeds/test5.ged"))

    def test5(self):
      result = [['I1', 'I14'], ['I9', 'I2', 'I10'], ['I13', 'I3'], [], [], ['I8']]
      self.assertEqual(result, us28("seeds/test6.ged"))

if __name__ == '__main__':
    unittest.main()