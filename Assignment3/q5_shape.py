import math


class Shape:
    id = 1

    def __init__(self):
        self.id = Shape.id
        Shape.id += 1

    def __repr__(self) -> str:
        return "id: " + str(self.id) + ", name: " + type(self).__name__

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
        return 2 * math.pi * self.radius

    def area(self):
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
        return 2 * math.sqrt((self.p**2) + (self.q**2))

    def area(self):
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
    # Test for id and class name
    s1 = Shape()
    assert repr(s1) == "id: 1, name: Shape"
    s2 = Shape()
    assert repr(s2) == "id: 2, name: Shape"

    # Test for area
    assert s1.area() == None

    # Test for perimeter
    assert s2.perimeter() == None


def test_circle():
    c1 = Circle(5)

    # Test for id and name of shape
    assert repr(c1) == "id: 3, name: Circle"

    # Test for perimeter
    assert abs(c1.perimeter() - 31.41593) < eps

    # Test for area
    assert abs(c1.area() - 78.53982) < eps


def test_ellipse():
    e1 = Ellipse(4, 5)
    e2 = Ellipse(6, 2)

    # Test for id and class name
    assert repr(e1) == "id: 4, name: Ellipse"
    assert repr(e2) == "id: 5, name: Ellipse"

    # Test for area
    assert abs(e1.area() - 62.83185) < eps
    assert abs(e2.area() - 37.69911) < eps

    # Test for eccentricity
    assert e1.eccentricity() == 3
    assert abs(e2.eccentricity() - 5.65685424949238) < eps


def test_rhombus():
    r1 = Rhombus(4, 6)

    # Test for id and class name
    assert repr(r1) == "id: 6, name: Rhombus"

    # Test for perimeter
    assert abs(r1.perimeter() - 14.42221) < eps

    # Test for area
    assert r1.area() == 12

    # Test for inradius
    assert abs(r1.inradius() - 1.664101) < eps
