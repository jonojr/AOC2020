
def trees_hit(map, x_slope, y_slope):
    x_pos = 0
    y_pos = 0
    hits = 0
    width = len(map[0])

    while y_pos < len(map):
        if map[y_pos][x_pos] == "#":
            hits += 1

        x_pos += x_slope
        y_pos += y_slope

        if x_pos >= width:
            x_pos -= width

    return hits


if __name__ == "__main__":
    with open("input.txt", "r") as input_file:
        map = input_file.read().split()

    possible_slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

    result = 1

    for x_slope, y_slope in possible_slopes:
        result *= trees_hit(map, x_slope, y_slope)

    print(result)
