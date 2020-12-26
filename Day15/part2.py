from collections import defaultdict

if __name__ == "__main__":
    starting_values = [2, 0, 1, 7, 4, 14, 18]

    last_spoken_time = defaultdict(lambda: 0)
    turn = 0
    last_spoken = None

    for position, value in enumerate(starting_values):
        last_spoken_time[last_spoken] = position + 1
        turn = position + 1
        last_spoken = value

    print(last_spoken_time)
    while turn < 30000000:
        turn += 1

        last_time = last_spoken_time[last_spoken]
        if last_time == 0:
            spoken = 0
        else:
            spoken = turn - last_time
        last_spoken_time[last_spoken] = turn
        last_spoken = spoken

    print(spoken)
