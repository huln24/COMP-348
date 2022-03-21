import math


class Shape:
    id = 1

    def __init__(self):
        self.id = Shape.id
        Shape.id += 1

    def __repr__(self) -> str:
        p = self.perimeter()
        if p is None:
            p = "undefined"
        else:
            p = f'{p:.5f}'

        a = self.area()
        if a is None:
            a = "undefined"
        else:
            a = f'{a:.5f}'

        return (
            str(self.id)
            + ": "
            + type(self).__name__
            + ", perimeter: " + p
            + ", area: " + a
        )

    def print(self):
        print(self)

    def perimeter(self):
        return None

    def area(self):
        return None


class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def perimeter(self):
        if self.radius < 0:
            return None
        return 2 * math.pi * self.radius

    def area(self):
        if self.radius < 0:
            return None
        return math.pi * (self.radius**2)


class Ellipse(Shape):
    def __init__(self, a, b):
        super().__init__()
        if a > b:
            self.a = a
            self.b = b
        else:
            self.b = a
            self.a = b

    def area(self):
        if self.a < 0 or self.b < 0:
            return None
        return math.pi * self.a * self.b

    def eccentricity(self):
        try:
            c = math.sqrt((self.a**2) - (self.b**2))
        except:
            return None
        else:
            return c


class Rhombus(Shape):
    def __init__(self, p, q):
        super().__init__()
        self.p = p
        self.q = q

    def perimeter(self):
        if self.p < 0 or self.q < 0:
            return None
        return 2 * math.sqrt((self.p**2) + (self.q**2))

    def area(self):
        if self.p < 0 or self.q < 0:
            return None
        return (self.p * self.q) / 2

    def inradius(self):
        try:
            r = (self.p * self.q) / self.perimeter()
        except:
            return None
        else:
            return r


# TESTS

# Precision testing value
eps = 1e-4


def test_shapes():
    s1 = Shape()
    s2 = Shape()

    # Test for id
    assert s1.id == 1
    assert s2.id == 2

    # Test for class name
    assert type(s1).__name__ == "Shape"

    # Test for area
    assert s1.area() is None

    # Test for perimeter
    assert s2.perimeter() is None

    assert repr(s1) == "1: Shape, perimeter: undefined, area: undefined"


def test_circle():
    c1 = Circle(5)

    # Test for id
    assert c1.id == 3

    # Test for class name
    assert type(c1).__name__ == "Circle"

    # Test for perimeter
    assert abs(c1.perimeter() - 31.41593) < eps

    # Test for area
    assert abs(c1.area() - 78.53982) < eps


def test_ellipse():
    e1 = Ellipse(4, 5)
    e2 = Ellipse(6, 2)
    e3 = Ellipse(-5, -3)

    # Test for id
    assert e1.id == 4
    assert e2.id == 5
    assert e3.id == 6

    # Test for class name
    assert type(e1).__name__ == "Ellipse"

    # Test for area
    assert abs(e1.area() - 62.83185) < eps
    assert abs(e2.area() - 37.69911) < eps

    # Test for eccentricity
    assert e1.eccentricity() == 3
    assert abs(e2.eccentricity() - 5.65685424949238) < eps
    assert e3.eccentricity() is None


def test_rhombus():
    r1 = Rhombus(4, 6)
    r2 = Rhombus(0, 0)

    # Test for id
    assert r1.id == 7
    assert r2.id == 8

    # Test for class name
    assert type(r1).__name__ == "Rhombus"

    # Test for perimeter
    assert abs(r1.perimeter() - 14.42221) < eps

    # Test for area
    assert r1.area() == 12

    # Test for inradius
    assert abs(r1.inradius() - 1.664101) < eps
    assert r2.inradius() is None
