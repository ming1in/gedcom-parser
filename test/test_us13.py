import unittest
import datetime
import sys
import os
sys.path.append(os.path.abspath('../src'))
import us13

class us13_test(unittest.TestCase):
    def test1(self):
        filename = "seeds/seed.ged" 
        ret = "All siblings are valid"
        self.assertEqual(us13.siblingsAgeGap(filename),ret)

    def test2(self):
        filename = "seeds/test1.ged" 
        ret = "All siblings are valid"
        self.assertEqual(us13.siblingsAgeGap(filename),ret)


    def test3(self):
        filename = "seeds/test2.ged" 
        ret = "All siblings are valid"
        self.assertEqual(us13.siblingsAgeGap(filename),ret)

    def test4(self):
        filename = "seeds/test5.ged" 
        ret = "All siblings are valid"
        self.assertEqual(us13.siblingsAgeGap(filename),ret)
    
    def test5(self):
        filename = "seeds/test13.ged" 
        ret = 'Individuals ', 'I14', ' and ', 'I15', ' are invalid.'
        self.assertEqual(us13.siblingsAgeGap(filename),ret)

if __name__ == '__main__':
        unittest.main() 
