
def count_differences(values):
    one_diff = 0
    three_diff = 0

    for i in range(1, len(values)):
        difference = values[i] - values[i-1]
        print(difference, values[i-1], values[i])
        if difference == 1:
            one_diff += 1
        if difference == 3:
            three_diff += 1

    return one_diff, three_diff


if __name__ == "__main__":
    with open("input.txt", 'r') as input_file:
        values = [0]
        values.extend([int(value) for value in input_file.read().split("\n")])

    values.sort()
    values.append(values[-1] + 3)

    one, three = count_differences(values)

    print(one * three)
