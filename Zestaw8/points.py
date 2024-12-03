
class Point:
    """Klasa reprezentująca punkt na płaszczyźnie"""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
       return f"({self.x}, {self.y})"

    def __repr__(self):
       return f"Point({self.x}, {self.y})"

    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self == other

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def __hash__(self):
        return hash((self.x, self.y))