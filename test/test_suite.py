'''
Created on 10/06/20
@author:   @arana23 - Aparajita Rana
Pledge:    I pledge my honor to abide by the Stevens Honor System
SSW555 - Testing Suite
Goal: Run all tests for all completed User Stories
'''
import unittest

''' 
ADD YOUR TEST FILES HERE 
FORMAT: from FILENAME import CLASSNAME
'''
from us01_test import us01_test
from us02_test import us02_test
from us03_test import us03_test
from us04_test import us04_test
#from us05_test import us05_test
#from us06_test import us06_test
from us07_test import us07_test
from us08_test import us08_test
from us09_test import us09_test
from us10_test import us10_test
#from us11_test import us11_test
from us12_test import us12_test
from us13_test import us13_test
from us14_test import us14_test
from us15_test import us15_test
from us16_test import us16_test
from us18_test import us18_test
from us19_test import us19_test
#from us21_test import us21_test
from us22_test import us22_test
from us23_test import us23_test
from us24_test import us24_test
from us25_test import us25_test
from us26_test import us26_test
from us27_test import us27_test
from us28_test import us28_test
from us29_test import us29_test
from us30_test import us30_test
from us31_test import us31_test
from us33_test import us33_test
#from us34_test import us34_test
from us35_test import us35_test
from us36_test import us36_test
from us37_test import us37_test
from us38_test import us38_test
from us39_test import us39_test
#from us40_test import us40_test
from us41_test import us41_test
from us42_test import us42_test
from us46_test import us46_test

# **ADD YOUR TEST FILES HERE**
tests = {
    us01_test,
    us02_test,
    us03_test,
    #us04_test,
    #us05_test,
    #us06_test,
    us07_test,
    us08_test,
    #us09_test,
    us10_test,
    #us11_test,
    us12_test,
    us13_test,
    us14_test, 
    us15_test, 
    us16_test,
    #us18_test, 
    us19_test, 
    #us21_test,
    us22_test,
    us23_test,
    us24_test, 
    us25_test,
    us26_test,
    us27_test,
    us28_test,
    us29_test, 
    us30_test,
    us31_test,
    us33_test,
    #us34_test,
    #us35_test,
    us36_test, 
    #us37_test,
    us38_test,
    us39_test,
    #us40_test,
    us41_test, 
    us42_test,
    us46_test,
}

test_suite = unittest.TestSuite()
for t in tests:
    test_suite.addTest(unittest.makeSuite(t))

# print all correct tests
runner = unittest.TextTestRunner()
runner.run(test_suite)
