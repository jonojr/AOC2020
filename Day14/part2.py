from collections import defaultdict


def floating_generator(value):
    if 'X' not in value:
        yield value
    else:
        yield from floating_generator(value.replace('X', '0', 1))
        yield from floating_generator(value.replace('X', '1', 1))


def apply_floating(value):
    results = [address for address in floating_generator(value)]

    return results


def apply_mask(value, mask):
    base = list(value)
    for i in range(len(value)):
        if mask[i] == '1':
            base[i] = '1'
        elif mask[i] == 'X':
            base[i] = 'X'


    return apply_floating("".join(base))


if __name__ == "__main__":
    with open("input.txt", 'r') as input_file:
        instructions = [instruction.split(" = ") for instruction in input_file.read().split("\n")]

    MEMORY = defaultdict(lambda: 0)
    MASK = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

    for instruction in instructions:
        if instruction[0] == 'mask':
            MASK = instruction[1]
        else:
            memory_address = int(instruction[0].strip("mem[]"))
            binary_address = f"{memory_address:036b}"

            value = int(instruction[1])

            masked_addresses = apply_mask(binary_address, MASK)

            for address in masked_addresses:
                MEMORY[address] = value


    print(MEMORY)

    print(f"Sum of all values in memory: {sum(MEMORY.values())}")
