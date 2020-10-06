import sys
import unittest
import os
sys.path.append(os.path.abspath('../src'))
os.chdir(os.path.abspath('../test/seeds'))
import us02


class Testuser02(unittest.TestCase):
    #all marriages after birth

    def test01(self):
        s = ""
        self.assertEquals(s, us02.user02("test1.ged"))

    def test02(self):
        s = ""
        self.assertEquals(s, us02.user02("test2.ged"))

    def test03(self):
        s = ""
        self.assertEquals(s, us02.user02("test3.ged"))
    def test04(self):
        s = ""
        self.assertEquals(s, us02.user02("test8.ged"))
    def test05(self):
        s = ""
        self.assertEquals(s, us02.user02("test5.ged"))

if __name__ == '__main__':
    unittest.main()
