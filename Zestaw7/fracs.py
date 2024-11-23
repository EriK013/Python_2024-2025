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
        if isinstance(other, Frac):
            return self.x == other.x and self.y == other.y
        elif isinstance(other, (int, float)):
            return float(self) == float(other)
        return NotImplemented

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        return float(self) < float(other)

    def __le__(self, other):
        return float(self) <= float(other)

    def __gt__(self, other):
        return float(self) > float(other)

    def __ge__(self, other):
        return float(self) >= float(other)

    def __add__(self, other):  # frac1 + frac2
        if isinstance(other, Frac):
            return Frac(self.x * other.y + other.x * self.y, self.y * other.y)
        elif isinstance(other, int):
            return Frac(self.x + other * self.y, self.y)
        elif isinstance(other, float):
            other_frac = Frac(*other.as_integer_ratio())
            return self + other_frac
        return NotImplemented

    __radd__ = __add__

    def __sub__(self, other):   # frac1 - frac2
        if isinstance(other, Frac):
            return Frac(self.x * other.y - other.x * self.y, self.y * other.y)
        elif isinstance(other, int):
            return Frac(self.x - other * self.y, self.y)
        elif isinstance(other, float):
            other_frac = Frac(*other.as_integer_ratio())
            return self - other_frac
        return NotImplemented

    def __rsub__(self, other):
        if isinstance(other, int):
            return Frac(other * self.y - self.x, self.y)
        elif isinstance(other, float):
            other_frac = Frac(*other.as_integer_ratio())
            return other_frac - self
        return NotImplemented


    def __mul__(self, other):   # frac1 * frac2
        if isinstance(other, Frac):
            return Frac(self.x * other.x, self.y * other.y)
        elif isinstance(other, int):
            return Frac(self.x * other, self.y)
        elif isinstance(other, float):
            other_frac = Frac(*other.as_integer_ratio())
            return self * other_frac
        return NotImplemented

    __rmul__ = __mul__

    def __truediv__(self, other):   # frac1 / frac2, Py3
        if isinstance(other, Frac):
            return Frac(self.x * other.y, self.y * other.x)
        elif isinstance(other, int):
            return Frac(self.x, self.y * other)
        elif isinstance(other, float):
            other_frac = Frac(*other.as_integer_ratio())
            return self / other_frac
        return NotImplemented

    def __rtruediv__(self, other):
        if isinstance(other, int):
            return Frac(self.y * other, self.x)
        elif isinstance(other, float):
            other_frac = Frac(*other.as_integer_ratio())
            return other_frac / self
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