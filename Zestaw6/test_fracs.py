import unittest
from fracs import *

class TestFracs(unittest.TestCase):
    def setUp(self):
        self.zero = Frac(0)
        self.one = Frac(1)
        self.f1 = Frac(1,2)
        self.f2 = Frac(1, -2)
        self.f3 = Frac(2,3)


    def test_str(self):
        self.assertEqual(str(self.zero), "0")
        self.assertEqual(str(self.one), "1")
        self.assertEqual(str(self.f1), "1/2")
        self.assertEqual(str(self.f2), "-1/2")


    def test_repr(self):
        self.assertEqual(repr(self.zero), "Frac(0, 1)")
        self.assertEqual(repr(self.one), "Frac(1, 1)")
        self.assertEqual(repr(self.f1), "Frac(1, 2)")
        self.assertEqual(repr(self.f2), "Frac(-1, 2)")

    def test_eq(self):
        self.assertTrue(self.zero == self.zero)
        self.assertTrue(self.one == self.one)
        self.assertFalse(self.zero == self.f1)
        self.assertFalse(self.f1 == self.f2)

    def test_ne(self):
        self.assertTrue(self.zero != self.f1)
        self.assertFalse(self.f2 != self.f2)
        self.assertTrue(self.f3 != self.f1)

    def test_lt(self):
        self.assertTrue(self.zero < self.one)
        self.assertTrue(self.f2 < self.f1)
        self.assertFalse(self.f3 < self.f1)

    def test_le(self):
        self.assertTrue(self.zero <= self.zero)
        self.assertTrue(self.one <= self.one)
        self.assertTrue(self.zero <= self.one)
        self.assertFalse(self.f3 <= self.f1)
        self.assertTrue(self.f2 <= self.f1)

    def test_gt(self):
        self.assertTrue(self.one > self.zero)
        self.assertTrue(self.f1 > self.zero)
        self.assertFalse(self.f2 > self.f1)
        self.assertTrue(self.f3 > self.f1)

    def test_ge(self):
        self.assertTrue(self.zero >= self.zero)
        self.assertTrue(self.one >= self.one)
        self.assertFalse(self.f1 >= self.f3)
        self.assertTrue(self.f1 >= self.f2)

    def test_add(self):
        self.assertEqual(self.zero + self.zero, Frac(0, 1))
        self.assertEqual(self.zero + self.one, Frac(1, 1))
        self.assertEqual(self.f1 + self.f2, Frac(0, 2))
        self.assertEqual(self.f1 + self.f3, Frac(7, 6))

    def test_sub(self):
        self.assertEqual(self.f1 - self.f2, Frac(2, 2))
        self.assertEqual(self.zero - self.one, Frac(-1, 1))
        self.assertEqual(self.f2 - self.f1, Frac(-2, 2))
        self.assertEqual(self.f3 - self.f1, Frac(1, 6))

    def test_mull(self):
        self.assertEqual(self.f1 * self.zero, Frac(0, 2))
        self.assertEqual(self.f1 * self.f2, Frac(-1, 4))
        self.assertEqual(self.f1 * self.f3, Frac(2,6))

    def test_truediv(self):
        self.assertEqual(self.zero / self.one, Frac(0, 1))
        self.assertEqual(self.f1 / self.f2, Frac(2, -2))
        self.assertEqual(self.f1 / self.f3, Frac(3, 4))

    def test_pos(self):
        self.assertEqual(+self.f1, self.f1)
        self.assertEqual(+self.one, self.one)

    def test_neg(self):
        self.assertEqual(-self.zero, self.zero)
        self.assertEqual(-self.f2, self.f1)
        self.assertEqual(-self.f3, Frac(-2, 3))

    def test_invert(self):
        self.assertEqual(~self.f3, Frac(3,2))
        self.assertEqual(~self.f1, Frac(2,1))
        self.assertEqual(~self.f2, Frac(-2,1))

    def test_float(self):
        self.assertEqual(float(self.zero), 0.0)
        self.assertEqual(float(self.one), 1.0)
        self.assertEqual(float(self.f1), 0.5)
        self.assertEqual(float(self.f2), -0.5)

    def test_hash(self):
        self.assertEqual(hash(self.zero), hash(Frac(0, 1)))
        self.assertEqual(hash(self.f1), hash(Frac(1, 2)))
        self.assertEqual(hash(self.f2), hash(Frac(-1,2)))

    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()