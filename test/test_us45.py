import unittest
import datetime
import sys
import os
sys.path.append(os.path.abspath('../src'))
from us45 import us45

class us44_test(unittest.TestCase):
    def test1(self):
        filename = "seeds/us45/seed.ged" 
        ret = 'I6'
        self.assertEqual(us45(filename),ret)

    def test2(self):
        filename = "seeds/us45/test3.ged" 
        ret = 'I2'
        self.assertEqual(us45(filename),ret)

   

if __name__ == '__main__':
        unittest.main() 
