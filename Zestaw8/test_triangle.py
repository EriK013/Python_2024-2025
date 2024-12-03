import unittest
from triangle import Triangle
from points import Point

class TestTriangle(unittest.TestCase):

    def test_init(self):
        with self.assertRaises(ValueError):
            Triangle(0, 0, 1, 1, 2, 2)  # Punkty współliniowe

    def test_str_and_repr(self):
        tr = Triangle(0, 0, 1, 0, 0, 1)
        self.assertEqual(str(tr), "[(0, 0), (1, 0), (0, 1)]")
        self.assertEqual(repr(tr), "Triangle(0, 0, 1, 0, 0, 1)")

    def test_eq(self):
        tr1 = Triangle(0, 0, 1, 0, 0, 1)
        tr2 = Triangle(1, 0, 0, 1, 0, 0)
        self.assertEqual(tr1, tr2)

    def test_center(self):
        tr = Triangle(0, 0, 6, 0, 0, 6)
        self.assertAlmostEqual(tr.center.x, 2)
        self.assertAlmostEqual(tr.center.y, 2)

    def test_area(self):
        tr = Triangle(0, 0, 6, 0, 0, 6)
        self.assertEqual(tr.area(), 18)

    def test_move(self):
        tr = Triangle(0, 0, 1, 0, 0, 1)
        tr.move(1, 1)
        self.assertEqual(tr, Triangle(1, 1, 2, 1, 1, 2))

    def test_make4(self):
        tr = Triangle(0, 0, 4, 0, 0, 4)
        sub_triangles = tr.make4()
        self.assertEqual(len(sub_triangles), 4)
        self.assertTrue(all(isinstance(t, Triangle) for t in sub_triangles))

    def test_from_points(self):
        p1, p2, p3 = Point(0, 0), Point(4, 0), Point(2, 3)
        triangle = Triangle.from_points((p1, p2, p3))
        self.assertEqual(triangle, Triangle(p1.x, p1.y, p2.x, p2.y, p3.x, p3.y))

    def test_bounding_box_properties(self):
        tr = Triangle(0, 0, 4, 0, 2, 3)

        self.assertEqual(tr.top, 0)
        self.assertEqual(tr.bottom, 3)
        self.assertEqual(tr.left, 0)
        self.assertEqual(tr.right, 4)

        self.assertEqual(tr.width, 4)
        self.assertEqual(tr.height, 3)

        self.assertEqual(tr.topleft, Point(0, 0))
        self.assertEqual(tr.bottomleft, Point(0, 3))
        self.assertEqual(tr.topright, Point(4, 0))
        self.assertEqual(tr.bottomright, Point(4, 3))
if __name__ == "__main__":
    unittest.main()
