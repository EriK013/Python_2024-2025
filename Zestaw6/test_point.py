import unittest
from point import *

class TestPoint(unittest.TestCase):
    def setUp(self):
        self.zero = Point(0, 0)
        self.p1 = Point(1, 2)
        self.p2 = Point(3, 4)
        self.p3 = Point(5, 6)
        self.p4 = Point(-1, 2)
        self.p5 = Point(-3, -4)
        self.p6 = Point(-1, 0)

    def test_str(self):
        self.assertEqual(str(self.p1), "(1, 2)")
        self.assertEqual(str(self.zero), "(0, 0)")

    def test_repr(self):
        self.assertEqual(repr(self.zero), "Point(0, 0)")
        self.assertEqual(repr(self.p1), "Point(1, 2)")
        self.assertEqual(repr(self.p6), "Point(-1, 0)")

    def test_eq(self):
        self.assertTrue(self.zero == self.zero)
        self.assertFalse(self.zero == self.p1)
        self.assertFalse(self.p1 == self.p4)
        self.assertFalse(self.p4 == self.p6)
        self.assertTrue(self.p1 == self.p1)

    def test_ne(self):
        self.assertTrue(self.zero != self.p1)
        self.assertFalse(self.p2 != self.p2)
        self.assertTrue(self.p3 != self.p4)

    def test_add(self):
        self.assertEqual(self.p1 + self.p2, Point(4, 6))
        self.assertEqual(self.p1 + self.p3, Point(6, 8))
        self.assertEqual(self.p1 + self.zero, self.p1)
        self.assertEqual(self.p1 + self.p4, Point(0, 4))

    def test_sub(self):
        self.assertEqual(self.p1 - self.p2, Point(-2, -2))
        self.assertEqual(self.p1 - self.p4, Point(2, 0))
        self.assertEqual(self.p1 - self.zero, self.p1)
        self.assertEqual(self.zero - self.p6, Point(1, 0))

    def test_mull(self):
       self.assertEqual(self.p1 * self.p2, Point(3, 8))
       self.assertEqual(self.p4 * self.zero, self.zero)
       self.assertEqual(self.p5 * self.p4, Point(3,-8))

    def test_cross(self):
        self.assertEqual(self.p4.cross(self.zero), 0)
        self.assertEqual(self.p1.cross(self.p2), -2)
        self.assertEqual(self.p4.cross(self.p6), 2)

    def test_length(self):
        self.assertEqual(self.p2.length(), 5)
        self.assertEqual(self.zero.length(), 0)
        self.assertEqual(self.p1.length(), self.p4.length())

    def test_hash(self):
        self.assertEqual(hash(self.zero), hash(Point(0, 0)))
        self.assertEqual(hash(self.p1), hash(Point(1, 2)))

    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()