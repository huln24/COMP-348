def lucas_numbers(n):
    if n in (1, 2):
        return []
    seq = [2, 1]
    sum = seq[-1] + seq[-2]
    while sum < n:
        seq.append(sum)
        sum = seq[-1] + seq[-2]
    print(seq)


# def test_lucas():
#    assert lucas_numbers(1) == []
#    assert lucas_numbers(2) == []
#    assert lucas_numbers(5) == [2, 1, 3, 4]


if __name__ == "__main__":
    lucas_numbers(5)
    # print(", ".join(map(str, lucas_numbers(8))))
    # $ coverage run -m pytest q2_lucas_sequence.py
    # $ coverage report
