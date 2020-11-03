import unittest
import datetime
import sys
import os
sys.path.append(os.path.abspath('../src'))
import us46

class us46_test(unittest.TestCase):
    def test1(self):
        filename = "seeds/seed.ged" 
        ret = [['I11'], ['I13']]
        self.assertEqual(us46.us46(filename),ret)

    def test2(self):
        filename = "seeds/test7.ged" 
        ret = [['I4'], ['I8']]
        self.assertEqual(us46.us46(filename),ret)


    def test3(self):
        filename = "seeds/test8.ged" 
        ret = [['I11'], ['I13']]
        self.assertEqual(us46.us46(filename),ret)


    def test4(self):
        filename = "seeds/test3.ged" 
        ret = []
        self.assertEqual(us46.us46(filename),ret)




if __name__ == '__main__':
        unittest.main() 
