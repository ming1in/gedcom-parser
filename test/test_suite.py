'''
Created on 10/06/20
@author:   @arana23 - Aparajita Rana
Pledge:    I pledge my honor to abide by the Stevens Honor System
SSW555 - Testing Suite
Goal: Run all tests for all completed User Stories
'''
from us42_test import us42_test
from us41_test import us41_test
from us36_test import us36_test
from us35_test import us35_test
from us30_test import us30_test
from us29_test import us29_test
from us25_test import us25_test
from us24_test import us24_test
from us18_test import us18_test
from us16_test import us16_test
from us13_test import us13_test
from us09_test import us09_test
from us08_test import us08_test
from us07_test import us07_test
from us01_test import us01_test
import unittest

''' 
ADD YOUR TEST FILES HERE 
FORMAT: from FILENAME import CLASSNAME
'''

# **ADD YOUR TEST FILES HERE**
tests = {
    us01_test, us07_test, us08_test,
    us09_test, us13_test, us16_test,
    us18_test, us24_test, us25_test,
    us29_test, us30_test, us35_test,
    us36_test, us41_test, us42_test
}

test_suite = unittest.TestSuite()
for t in tests:
    test_suite.addTest(unittest.makeSuite(t))

# print all correct tests
runner = unittest.TextTestRunner()
runner.run(test_suite)
