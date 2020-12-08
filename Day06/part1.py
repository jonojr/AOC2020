from functools import reduce


def calculate_group_answers(group):
    group_answers = group.split()
    answer_sets = map(set, group_answers)
    all_answers = reduce(lambda a, b: a | b, answer_sets)
    return len(all_answers)


if __name__ == "__main__":
    with open("input.txt", 'r') as input_file:
        answers = input_file.read().split("\n\n")

    total = 0
    for group in answers:
        total += calculate_group_answers(group)

    print(total)
