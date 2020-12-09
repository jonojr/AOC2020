
class Computer:
    def __init__(self, code):
        self.code = code
        self.pc = 0
        self.acc = 0

        self.visited_addresses = set()

    def step(self):
        self.visited_addresses.add(self.pc)

        try:
            operation, arg = self.code[self.pc]
        except IndexError:
            # print("PC not in valid memory addresses.")
            return self.pc

        if operation == 'nop':
            self.pc += 1
            return self.pc
        if operation == 'acc':
            self.pc += 1
            self.acc += arg
            return self.pc
        if operation == 'jmp':
            self.pc += arg
            return self.pc

    def run_until_repeat(self):
        last_address = -1
        while last_address not in self.visited_addresses:
            last_address = self.step()

        return self.acc

    def successful(self):
        self.run_until_repeat()
        # print(self.pc)
        return self.pc >= len(self.code) - 1


def generate_all_possible_programs(code):
    for i in range(len(code)):
        tmp = code[:]
        if code[i][0] == 'jmp':
            tmp[i] = ('nop', tmp[i][1])
            yield tmp
        elif code[i][0] == 'nop':
            tmp[i] = ('jmp', tmp[i][1])
            yield tmp


if __name__ == "__main__":
    with open("input.txt", 'r') as input_file:
        code = [(line.split()[0], int(line.split()[1])) for line in input_file.read().split("\n")]

    for program in generate_all_possible_programs(code):
        computer = Computer(program)
        if computer.successful():
            print(f"Successful: {computer.acc}")
            break
