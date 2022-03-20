def lucas_sequence_1(n):
    """Compute lucas sequence

    Parameters
    ----------
    n: int
        Number of lucas number

    Returns
    -------
    A list of the n first number of lucas sequence
    """
    sequence = []
    for i in range(n):
        if i == 0:
            sequence.append(2)
        elif i == 1:
            sequence.append(1)
        else:
            sequence.append(sequence[i - 1] + sequence[i - 2])
    return sequence


def test_lucas_sequence():
    assert lucas_sequence_1(1) == [2]
    assert lucas_sequence_1(2) == [2, 1], "Sequence should match"
    assert lucas_sequence_1(3) == [2, 1, 3]
    assert lucas_sequence_1(7) == [2, 1, 3, 4, 7, 11, 18]


if __name__ == "__main__":
    # $ coverage run -m pytest q2_lucas_sequence.py
    # $ coverage report
    #   Name                   Stmts   Miss  Cover
    #   ------------------------------------------
    #   q2_lucas_sequence.py      14      0   95%
    #   ------------------------------------------
    #   TOTAL                     14      0   95%
    print(lucas_sequence_1(5))
