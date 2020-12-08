
def trees_hit(map):
    x_pos = 0
    y_pos = 0
    hits = 0
    width = len(map[0])

    while y_pos < len(map):
        if map[y_pos][x_pos] == "#":
            hits += 1

        x_pos += 3
        y_pos += 1

        if x_pos >= width:
            x_pos -= width

    return hits


if __name__ == "__main__":
    with open("input.txt", "r") as input_file:
        map = input_file.read().split()


    print(trees_hit(map))