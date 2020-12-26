from collections import defaultdict

def apply_mask(value, mask):
    result = list(value)
    for i in range(len(value)):
        if mask[i] == '0':
            result[i] = '0'
        elif mask[i] == '1':
            result[i] = '1'

    return "".join(result)


if __name__ == "__main__":
    with open("input.txt", 'r') as input_file:
        instructions = [instruction.split(" = ") for instruction in input_file.read().split("\n")]

    MEMORY = defaultdict(lambda: 0)
    MASK = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

    for instruction in instructions:
        if instruction[0] == 'mask':
            MASK = instruction[1]
        else:
            memory_address = instruction[0].strip("mem[]")

            initial_value = f"{int(instruction[1]):036b}"
            masked_value = apply_mask(initial_value, MASK)

            MEMORY[memory_address] = int(masked_value, 2)


    print(MEMORY)

    print(f"Sum of all values in memory: {sum(MEMORY.values())}")
