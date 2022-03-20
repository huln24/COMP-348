def lucas_numbers(n):
    if n in (1, 2):
        return []
    seq = [2, 1]
    sum = seq[-1] + seq[-2]
    while sum < n:
        seq.append(sum)
        sum = seq[-1] + seq[-2]
    return seq


if __name__ == "__main__":

    print(", ".join(map(str, lucas_numbers(8))))
