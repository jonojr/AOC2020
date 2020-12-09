
class Computer:
    def __init__(self, code):
        self.code = code
        self.pc = 0
        self.acc = 0

        self.visited_addresses = set()

    def step(self):
        operation, arg = code[self.pc]
        self.visited_addresses.add(self.pc)

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


if __name__ == "__main__":
    with open("input.txt", 'r') as input_file:
        code = [(line.split()[0], int(line.split()[1])) for line in input_file.read().split("\n")]

    computer = Computer(code)
    print(computer.run_until_repeat())



