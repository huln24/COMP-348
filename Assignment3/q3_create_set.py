def sequence_to_set(sequence):
    my_set = []
    unique_items = dict()
    for item in sequence:
        if item not in unique_items:
            unique_items[item] = 1
            my_set.append(item)
    return my_set


def test_seq_to_set():
    assert sequence_to_set((1, 2, 3, 1, 4, 5, 5)) == [1, 2, 3, 4, 5]
    assert sequence_to_set([5, 4, 4, 3, 3, 3, 2, 2, 1]) == [5, 4, 3, 2, 1]


if __name__ == "__main__":
    print(sequence_to_set((1, 2, 3, 1, 4, 5, 5)))
    print(sequence_to_set([5, 4, 4, 3, 3, 3, 2, 2, 1]))
# $ coverage run -m pytest q2_lucas_sequence.py
# $ coverage report
