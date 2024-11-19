import math

class Frac:
    """Klasa reprezentująca ułamek."""

    def __init__(self, x=0, y=1):
        if y == 0:
            raise ValueError("Nie można dzielić przez zero!")
        nwd = math.gcd(x, y)
        self.x = x // nwd
        self.y = y // nwd

        if self.y < 0:
            self.x = -self.x
            self.y = -self.y

    def __str__(self):         # zwraca "x/y" lub "x" dla y=1
        if self.y == 1:
            return f"{self.x}"
        return f"{self.x}/{self.y}"

    def __repr__(self):         # zwraca "Frac(x, y)"
        return f"Frac({self.x}, {self.y})"

    def __eq__(self, other):    # Py2.7 i Py3
        return isinstance(other, Frac) and self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        return isinstance(other, Frac) and self.x * other.y < other.x * self.y

    def __le__(self, other):
        return isinstance(other, Frac) and self.x * other.y <= other.x * self.y

    def __gt__(self, other):
        return isinstance(other, Frac) and self.x * other.y > other.x * self.y

    def __ge__(self, other):
        return isinstance(other, Frac) and self.x * other.y >= other.x * self.y

    def __add__(self, other):  # frac1 + frac2
        if isinstance(other, Frac):
            return Frac(self.x * other.y + other.x * self.y, self.y * other.y)
        return NotImplemented

    def __sub__(self, other):   # frac1 - frac2
        if isinstance(other, Frac):
            return Frac(self.x * other.y - other.x * self.y, self.y * other.y)
        return NotImplemented

    def __mul__(self, other):   # frac1 * frac2
        if isinstance(other, Frac):
            return Frac(self.x * other.x, self.y * other.y)
        return NotImplemented

    def __truediv__(self, other):   # frac1 / frac2, Py3
        if isinstance(other, Frac):
            return Frac(self.x * other.y, self.y * other.x)
        return NotImplemented

    # operatory jednoargumentowe
    def __pos__(self):  # +frac = (+1)*frac
        return self

    def __neg__(self):  # -frac = (-1)*frac
        return Frac(-self.x, self.y)

    def __invert__(self):  # odwrotnosc: ~frac
        return Frac(self.y, self.x)

    def __float__(self):        # float(frac)
        return self.x / self.y

    def __hash__(self):
        return hash(float(self))   # immutable fracs
        # w Pythonie set([2]) == set([2.0])
        # chcemy set([2]) == set([Frac(2)])