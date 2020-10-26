import unittest
import datetime
import sys
import os
sys.path.append(os.path.abspath('../src'))
import us10

class us10_test(unittest.TestCase):
    def test1(self):
        filename = "seeds/seed.ged" 
        ret = "All marriages at acceptable age!"
        self.assertEqual(us10.marriedTooYoung(filename),ret)

    def test2(self):
        filename = "seeds/test7.ged" 
        ret = "All marriages at acceptable age!"
        self.assertEqual(us10.marriedTooYoung(filename),ret)


    def test3(self):
        filename = "seeds/test18.ged" 
        ret = "All marriages at acceptable age!"
        self.assertEqual(us10.marriedTooYoung(filename),ret)


    def test4(self):
        filename = "seeds/test19.ged" 
        ret = "The following people have marriage before the age of 14: Husbands[] Wives: ['I7']"
        self.assertEqual(us10.marriedTooYoung(filename),ret)

    
    def test5(self):
        filename = "seeds/test20.ged" 
        ret = "The following people have marriage before the age of 14: Husbands['I4', 'I4'] Wives: ['I5', 'I7']"
        self.assertEqual(us10.marriedTooYoung(filename),ret)


if __name__ == '__main__':
        unittest.main() 
