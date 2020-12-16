import itertools

WINDOW_SIZE = 25


def generate_possible_values(values, position):
    window_values = values[position - WINDOW_SIZE:position]
    return map(lambda a: a[0] + a[1], itertools.combinations(window_values, 2))


def test_contiguous(values, position, search_number):
    sum = 0
    start_position = position
    end_position = position

    while sum < search_number:
        sum += values[end_position]
        end_position += 1

    if sum == search_number:
        print(f"Found continguous that adds to {sum}, {values[start_position:end_position]}")
        return values[start_position:end_position]

    return []

if __name__ == "__main__":
    with open("input.txt", 'r') as input_file:
        values = [int(value) for value in input_file.read().split("\n")]

    invalid_number = None
    for i in range(len(values)-25):
        if values[WINDOW_SIZE + i] not in generate_possible_values(values, WINDOW_SIZE + i):
            print(values[WINDOW_SIZE + i])
            invalid_number = values[WINDOW_SIZE + i]
            break

    print(f"Found invalid number: {invalid_number}")

    for i in range(len(values)):
        result = test_contiguous(values, i, invalid_number)

        if result:
            result.sort()
            print(f"Weakness={result[0] + result[-1]}")
            break
