from points import Point

class Triangle:
    """Klasa reprezentująca trójkąty na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)
        self.pt3 = Point(x3, y3)
        if self._is_collinear():
            raise ValueError("Punkty są współliniowe, trójkąt nie może istnieć.")

    @classmethod
    def from_points(cls, points):
        """Tworzy trójkąt z listy lub krotki zawierającej trzy punkty."""
        if len(points) != 3:
            raise ValueError("Musisz podać dokładnie trzy punkty.")
        return cls(points[0].x, points[0].y, points[1].x, points[1].y, points[2].x, points[2].y)

    def _is_collinear(self):
        """Sprawdza, czy punkty są współliniowe."""
        return (self.pt2.x - self.pt1.x) * (self.pt3.y - self.pt1.y) == (self.pt3.x - self.pt1.x) * (self.pt2.y - self.pt1.y)

    @property
    def top(self):
        return min(self.pt1.y, self.pt2.y, self.pt3.y)

    @property
    def bottom(self):
        return max(self.pt1.y, self.pt2.y, self.pt3.y)

    @property
    def left(self):
        return min(self.pt1.x, self.pt2.x, self.pt3.x)

    @property
    def right(self):
        return max(self.pt1.x, self.pt2.x, self.pt3.x)

    @property
    def width(self):
        return self.right - self.left

    @property
    def height(self):
        return self.bottom - self.top

    @property
    def topleft(self):
        return Point(self.left, self.top)

    @property
    def bottomleft(self):
        return Point(self.left, self.bottom)

    @property
    def topright(self):
        return Point(self.right, self.top)

    @property
    def bottomright(self):
        return Point(self.right, self.bottom)

    @property
    def center(self):
        cx = (self.pt1.x + self.pt2.x + self.pt3.x) / 3
        cy = (self.pt1.y + self.pt2.y + self.pt3.y) / 3
        return Point(cx, cy)

    def __str__(self):
        return f"[{self.pt1}, {self.pt2}, {self.pt3}]"

    def __repr__(self):
        return f"Triangle({self.pt1.x}, {self.pt1.y}, {self.pt2.x}, {self.pt2.y}, {self.pt3.x}, {self.pt3.y})"

    def __eq__(self, other):
        if not isinstance(other, Triangle):
            return NotImplemented
        return set([self.pt1, self.pt2, self.pt3]) == set([other.pt1, other.pt2, other.pt3])

    def __ne__(self, other):
        return not self == other

    def area(self):
        return abs(
            (self.pt1.x * (self.pt2.y - self.pt3.y) +
             self.pt2.x * (self.pt3.y - self.pt1.y) +
             self.pt3.x * (self.pt1.y - self.pt2.y)) / 2
        )

    def move(self, x, y):
        self.pt1.move(x, y)
        self.pt2.move(x, y)
        self.pt3.move(x, y)

    def make4(self):
        mid1 = Point((self.pt1.x + self.pt2.x) / 2, (self.pt1.y + self.pt2.y) / 2)
        mid2 = Point((self.pt2.x + self.pt3.x) / 2, (self.pt2.y + self.pt3.y) / 2)
        mid3 = Point((self.pt3.x + self.pt1.x) / 2, (self.pt3.y + self.pt1.y) / 2)

        return (
            Triangle(self.pt1.x, self.pt1.y, mid1.x, mid1.y, mid3.x, mid3.y),
            Triangle(mid1.x, mid1.y, self.pt2.x, self.pt2.y, mid2.x, mid2.y),
            Triangle(mid3.x, mid3.y, mid2.x, mid2.y, self.pt3.x, self.pt3.y),
            Triangle(mid1.x, mid1.y, mid2.x, mid2.y, mid3.x, mid3.y),
        )
