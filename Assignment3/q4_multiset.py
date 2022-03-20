from ast import Pass


class Multiset:
    def __init__(self):
        self.data = []

    def add(self, n):
        self.data.append(n)

    def remove(self, n):
        # list of indexes to be removed
        to_be_deleted = []

        # Find all occurences of element to be removed
        for i, v in enumerate(self.data):
            if v == n:
                to_be_deleted.append(i)

        # remove data at indexes to be deleted starting from end
        # because else every removal shifts elements to the left
        # which would change initial index of the elements to be removed
        for i in reversed(to_be_deleted):
            del self.data[i]

    def m(self, n):
        count = 0
        for i in self.data:
            if i == n:
                count += 1
        return count

    def union(self, s2):
        self.m()

    # Represents Multiset object like a set object
    def __repr__(self) -> str:
        elts = ", ".join(map(str, self.data))
        return "{" + elts + "}"


def test_multiset():
    s = Multiset()

    # Test add elements
    s.add(1)
    assert repr(s) == "{1}"
    s.add(1)
    s.add(2)
    assert repr(s) == "{1, 1, 2}"

    # Test multiplicity
    assert s.m(1) == 2
    assert s.m(3) == 0

    # Test remove element
    s.remove(1)
    assert repr(s) == "{2}"
