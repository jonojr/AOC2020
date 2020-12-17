import sys
from collections import defaultdict

MEMOIZED_VALUES = defaultdict(lambda: 0)

MEMOIZED_VALUES[0] = 1


if __name__ == "__main__":
    sys.setrecursionlimit(9000)
    with open("input.txt", 'r') as input_file:
        values = [0]
        values.extend([int(value) for value in input_file.read().split("\n")])

    values.sort()
    values.append(values[-1] + 3)

    print(values)

    for value in values:
        if value != 0:
            MEMOIZED_VALUES[value] = sum([MEMOIZED_VALUES[value-1], MEMOIZED_VALUES[value-2], MEMOIZED_VALUES[value-3]])

    print(MEMOIZED_VALUES)
    print(MEMOIZED_VALUES[values[-1]])
