from itertools import combinations


with open("input.txt", "r") as input_file:
    expenses = input_file.read().split()
    expenses = [int(expense) for expense in expenses]

all_combinations = combinations(expenses, 2)
for combination in all_combinations:
    if combination[0] + combination[1] == 2020:
        print(combination[0] * combination[1])
