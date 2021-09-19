# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testLengthGreaterThan200(self): 
        self.assertEqual(classifyTriangle(201,201,300),'InvalidInput')

    def testLengthLessThan0(self): 
        self.assertEqual(classifyTriangle(-2,-3,-12),'InvalidInput')

    def testInteger(self):
        self.assertEqual(classifyTriangle(1.43,2.34,2.99), 'InvalidInput')

    def testValidTriangle(self): 
        self.assertEqual(classifyTriangle(4,6,11), 'NotATriangle')
    
    def testScaleneTriangle(self): 
        self.assertEqual(classifyTriangle(2,3,4), 'Scalene')

    def testIsocelesTriangle(self): 
        self.assertEqual(classifyTriangle(2,2,3),'Isoceles')

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

