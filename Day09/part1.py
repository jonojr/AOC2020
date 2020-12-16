import itertools

WINDOW_SIZE = 25


def generate_possible_values(values, position):
    window_values = values[position - WINDOW_SIZE:position]
    return map(lambda a: a[0] + a[1], itertools.combinations(window_values, 2))


if __name__ == "__main__":
    with open("input.txt", 'r') as input_file:
        values = [int(value) for value in input_file.read().split("\n")]

    for i in range(len(values)-25):
        if values[WINDOW_SIZE + i] not in generate_possible_values(values, WINDOW_SIZE + i):
            print(values[WINDOW_SIZE + i])
            break
