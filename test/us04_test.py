import unittest
import datetime
import sys
import os
sys.path.append(os.path.abspath('../src'))
import us04

class us04_test(unittest.TestCase):
    def test1(self):
        filename = "seeds/test14.ged" 
        ret = "All marraiges ar valid."
        self.assertEqual(us04.marriageBeforeDivorce(filename),ret)

    def test2(self):
        filename = "seeds/test17.ged" 
        ret = "F2 is invalid."
        self.assertEqual(us04.marriageBeforeDivorce(filename),ret)

    def test3(self):
        filename = "seeds/test5.ged" 
        ret = "All marraiges ar valid."
        self.assertEqual(us04.marriageBeforeDivorce(filename),ret)

    def test4(self):
        filename = "seeds/test7.ged" 
        ret = "All marraiges ar valid."
        self.assertEqual(us04.marriageBeforeDivorce(filename),ret)
    def test5(self):
        filename = "seeds/test18.ged" 
        ret = "All marraiges ar valid."
        self.assertEqual(us04.marriageBeforeDivorce(filename),ret)

if __name__ == '__main__':
        unittest.main() 
