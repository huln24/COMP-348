from ast import Pass


class MultisetIterator:
    def __init__(self, multiset):
        pass


class Multiset:
    def __init__(self, *args):
        self.data = list(args)

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
        ms1 = self.multiplem()
        ms2 = s2.multiplem()

        for key, value in ms2.items():
            if key in ms1:
                ms1[key] = max(ms1[key], value)
            else:
                ms1[key] = value

        m = Multiset()
        for value, count in ms1.items():
            m.add_times(value, count)
        return m

    def intersection(self, s2):
        d = dict()
        for i in self.data:
            if i in d:
                continue
            if i in s2.data:
                d[i] = min(self.m(i), s2.m(i))

        m = Multiset()
        for value, count in d.items():
            m.add_times(value, count)
        return m

    def difference(self, s2):
        d = dict()
        for i in s2.data:
            if i in d:
                continue
            d[i] = s2.m(i)

        for value, count in d.items():
            self.remove_times(value, count)

    def remove_times(self, el, count):
        for i in range(count):
            if el not in self.data:
                break
            self.data.remove(el)

    def add_times(self, value, count):
        for _ in range(count):
            self.add(value)

    def multiplem(self):
        d = dict()
        for el in self.data:
            m = self.m(el)
            d[el] = m
        return d

    # def __iter__(self):
    #   return iter(self.data)

    # Represents Multiset object like a set object
    def __repr__(self) -> str:
        elts = ", ".join(map(str, self.data))
        return "{" + elts + "}"


# Test add elements
def test_add():
    s = Multiset()
    s.add(1)
    assert repr(s) == "{1}"
    s.add(1)
    s.add(2)
    assert repr(s) == "{1, 1, 2}"


# Test multiplicity
def test_m():
    s = Multiset(1, 1, 2)
    assert s.m(1) == 2
    assert s.m(3) == 0


# Test remove element
def test_remove():
    s = Multiset(1, 1, 2)
    s.remove(1)
    assert repr(s) == "{2}"


# Test union
def test_union():
    s1 = Multiset(1, 2)
    s2 = Multiset(2, 2, 3)
    assert repr(s1) == "{1, 2}"
    assert repr(s2) == "{2, 2, 3}"
    s3 = s1.union(s2)
    assert repr(s3) == "{1, 2, 2, 3}"


# Test intersection
def test_intersection():
    ms1 = Multiset(1, 1, 2, 2, 3)
    ms2 = Multiset(2, 2, 2, 3, 4)
    ms3 = ms1.intersection(ms2)
    assert repr(ms3) == "{2, 2, 3}"


# Test difference
def test_difference():
    ms1 = Multiset(1, 1, 1, 2, 2, 3)
    ms2 = Multiset(1, 2, 2, 2)
    ms1.difference(ms2)
    assert repr(ms1) == "{1, 1, 3}"


if __name__ == "__main__":
    test_add()
    test_remove()
    test_m()
    test_union()
    test_intersection()
    test_difference()
    
    # $ coverage run -m pytest q2_lucas_sequence.py
    # $ coverage report
