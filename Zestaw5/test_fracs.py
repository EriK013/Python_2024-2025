import unittest
from fracs import *

class TestFractions(unittest.TestCase):
    def setUp(self):
        self.zero = [0, 1]
        self.f1 = [-1, 2]      # -1/2
        self.f2 = [1, -2]      # -1/2 (niejednoznaczność)
        self.f3 = [0, 1]       # zero
        self.f4 = [0, 2]       # zero (niejednoznaczność)
        self.f5 = [3, 1]       # 3
        self.f6 = [6, 2]       # 3 (niejednoznaczność)

    def test_add_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])

    def test_sub_frac(self):
        self.assertEqual(sub_frac([1, 2], [1, 3]), [1, 6])
        self.assertEqual(sub_frac([3, 4], [1, 4]), [1, 2])
        self.assertEqual(sub_frac(self.zero, self.f5), [-3, 1])
        self.assertEqual(sub_frac(self.zero, self.f1), [1, 2])

    def test_mul_frac(self):
        self.assertEqual(mul_frac([2, 3], [3, 4]), [1, 2])
        self.assertEqual(mul_frac([-1, 3], [3, 2]), [-1, 2])
        self.assertEqual(mul_frac(self.zero, self.f2), [0, -1])

    def test_div_frac(self):
        self.assertEqual(div_frac([1, 2], [3, 4]), [2, 3])

    def test_is_positive(self):
        self.assertTrue(is_positive([1, 2]))
        self.assertFalse(is_positive([-1, 2]))
        self.assertTrue(is_positive([5, 1]))
        self.assertFalse(is_positive([1, -2]))

    def test_is_zero(self):
        self.assertFalse(is_zero([1, 2]))
        self.assertFalse(is_zero([-1, 2]))
        self.assertTrue(is_zero([0, 1]))

    def test_cmp_frac(self):
        self.assertEqual(cmp_frac([1, 2], [1, 3]), 1)
        self.assertEqual(cmp_frac([2, 4], [1, 2]), 0)
        self.assertEqual(cmp_frac([1, 3], [3, 2]), -1)

    def test_frac2float(self):
        self.assertEqual(frac2float(self.f1), -0.5)
        self.assertEqual(frac2float(self.f5), 3.0)
        self.assertEqual(frac2float(self.zero), 0.0)

    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()
