from copy import deepcopy


def find_next_seat_in_direction(floor_map, x, y, x_direction, y_direction):
    x_pos = x + x_direction
    y_pos = y + y_direction

    y_len = len(floor_map)
    x_len = len(floor_map[y])

    while 0 <= x_pos < x_len and 0 <= y_pos < y_len:
        if floor_map[y_pos][x_pos] == 'L':
            return (x_pos, y_pos)

        x_pos += x_direction
        y_pos += y_direction

    return None



def generate_local_positions(floor_map, x, y):
    result = []

    result.append(find_next_seat_in_direction(floor_map, x, y, 1, 0))
    result.append(find_next_seat_in_direction(floor_map, x, y, 1, 1))
    result.append(find_next_seat_in_direction(floor_map, x, y, 1, -1))
    result.append(find_next_seat_in_direction(floor_map, x, y, 0, 1))

    result.append(find_next_seat_in_direction(floor_map, x, y, -1, 0))
    result.append(find_next_seat_in_direction(floor_map, x, y, -1, -1))
    result.append(find_next_seat_in_direction(floor_map, x, y, -1, 1))
    result.append(find_next_seat_in_direction(floor_map, x, y, 0, -1))

    result = filter(lambda a: bool(a), result)
    return result


def generate_all_positions(floor_map):
    result = {}

    for y in range(len(floor_map)):
        for x in range(len(floor_map[y])):
            result[(x, y)] = list(generate_local_positions(floor_map, x, y))

    return result


def calculate_new_value(floor_map, seat_mapping, xpos, ypos):
    current_value = floor_map[ypos][xpos]
    if current_value == '.':
        return '.'

    count = 0
    for x, y in seat_mapping[(xpos, ypos)]:
        if floor_map[y][x] == '#':
            count += 1

    if current_value == 'L' and count == 0:
        return '#'

    if current_value == '#' and count >= 5:
        return 'L'

    return current_value


def calculate_next_floor(floor_map, seat_mapping):
    new_map = deepcopy(floor_map)
    for y in range(len(floor_map)):
        for x in range(len(floor_map[y])):
            new_map[y][x] = calculate_new_value(floor_map, seat_mapping, x, y)

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

    print("Calculating all adjacent seats.")
    generated_adjacent_seats = generate_all_positions(values)

    previous_value = None
    current_value = values

    print("Iterating until we stabilise.")
    i = 0
    while current_value != previous_value:
        previous_value = current_value
        current_value = calculate_next_floor(previous_value, generated_adjacent_seats)
        i += 1

        if i % 500 == 0:
            print(f"generation: {i}")

    print(current_value)
    print(count_occupied(current_value))
