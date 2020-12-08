from math import ceil


def calculate_position(boarding_pass):
    x_position = list(range(128))
    y_position = list(range(8))
    for character in boarding_pass:
        if character == 'F':
            x_position = x_position[:len(x_position)//2]
        elif character == 'B':
            x_position = x_position[ceil(len(x_position) / 2):]

        if character == 'L':
            y_position = y_position[:len(y_position)//2]
        elif character == 'R':
            y_position = y_position[ceil(len(y_position) / 2):]

    return x_position[0], y_position[0]


if __name__ == "__main__":
    with open("input.txt", 'r') as input_file:
        boarding_passes = input_file.read().split()

    highest_ID = 0
    for boarding_pass in boarding_passes:
        x, y = calculate_position(boarding_pass)
        seat_id = x * 8 + y

        if seat_id > highest_ID:
            highest_ID = seat_id

    print(highest_ID)