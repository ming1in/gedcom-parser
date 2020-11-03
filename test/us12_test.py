import unittest
import datetime
import sys
import os
sys.path.append(os.path.abspath('../src'))
import us12

class us12_test(unittest.TestCase):
    def test1(self):
        filename = "seeds/test121.ged" 
        ret = ['I2']
        self.assertEqual(us12.us12(filename),ret)

    def test2(self):
        filename = "seeds/seed.ged" 
        ret = "All parents are an acceptable age"
        self.assertEqual(us12.us12(filename),ret)

    def test3(self):
        filename = "seeds/test123.ged" 
        ret = ['I2', 'I7']
        self.assertEqual(us12.us12(filename),ret)


    def test4(self):
        filename = "seeds/test124.ged" 
        ret = ['I6']
        self.assertEqual(us12.us12(filename),ret)




if __name__ == '__main__':
        unittest.main() 
