from copy import deepcopy


def generate_local_positions(x, y, x_max, y_max):
    result = [(x-1, y), (x, y-1), (x+1, y), (x, y+1), (x-1, y-1), (x-1, y+1), (x+1, y+1), (x+1, y-1)]

    result = filter(lambda a: (0 <= a[0] < x_max) and (0 <= a[1] < y_max), result)
    return result


def calculate_new_value(floor_map, xpos, ypos):
    current_value = floor_map[ypos][xpos]
    if current_value == '.':
        return '.'

    count = 0
    for x, y in generate_local_positions(xpos, ypos, len(floor_map[0]), len(floor_map)):
        if floor_map[y][x] == '#':
            count += 1

    if current_value == 'L' and count == 0:
        return '#'

    if current_value == '#' and count >= 4:
        return 'L'

    return current_value


def calculate_next_floor(floor_map):
    new_map = deepcopy(floor_map)
    for y in range(len(floor_map)):
        for x in range(len(floor_map[y])):
            new_map[y][x] = calculate_new_value(floor_map, x, y)

    return new_map


def count_occupied(floor_map):
    total = 0
    for y in range(len(floor_map)):
        for x in range(len(floor_map[y])):
            if floor_map[y][x] == '#':
                total += 1
    return total


if __name__ == "__main__":
    with open("input.txt", 'r') as input_file:
        values = [list(row) for row in input_file.read().split("\n")]

    previous_value = None
    current_value = values

    print("Iterating until we stabilise.")
    while current_value != previous_value:
        previous_value = current_value
        current_value = calculate_next_floor(previous_value)

    print(current_value)
    print(count_occupied(current_value))
