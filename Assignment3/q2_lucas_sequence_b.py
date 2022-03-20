def lucas_generator():
    i = 0
    while True:
        if i == 0:
            a = 2
            yield a
        elif i == 1:
            b = 1
            yield b
        else:
            yield a + b
            a, b = b, a + b
        i += 1


def lucas_sequence_2(n):
    seq = []
    for num in lucas_generator():
        if len(seq) == n:
            break
        seq.append(num)
    return seq


def test_lucas_sequence():
    assert lucas_sequence_2(1) == [2]
    assert lucas_sequence_2(2) == [2, 1], "Sequence should match"
    assert lucas_sequence_2(3) == [2, 1, 3]
    assert lucas_sequence_2(7) == [2, 1, 3, 4, 7, 11, 18]


if __name__ == "__main__":
    # $ coverage run -m pytest q2_lucas_sequence.py
    # $ coverage report
    #   Name                   Stmts   Miss  Cover
    #   ------------------------------------------
    #   q2_lucas_sequence.py      14      0   95%
    #   ------------------------------------------
    #   TOTAL                     14      0   95%
    print(lucas_sequence_2(7))
