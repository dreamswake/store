import unittest
from Demo.calc import Calc
class TestCalc2(unittest.TestCase):
    def testMutiply(self):
        c = Calc()
        a = 5
        b = 6
        s = 30
        sum = c.Multiply(a,b)
        self.assertEqual(s,sum)

    def testMutiply1(self):
        c = Calc()
        a = -5
        b = 6
        s = -30
        sum = c.Multiply(a,b)
        self.assertEqual(s,sum)

    def testMutiply2(self):
        c = Calc()
        a = 5
        b = -6
        s = -30
        sum = c.Multiply(a,b)
        self.assertEqual(s,sum)

    def testMutiply3(self):
        c = Calc()
        a = -5
        b = -6
        s = 30
        sum = c.Multiply(a,b)
        self.assertEqual(s,sum)













