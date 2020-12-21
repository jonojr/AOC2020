
class Ship:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.facing_index = 1

        self.HEADINGS = ['N', 'E', 'S', 'W']

    def move(self, instruction):
        operation = instruction[0]
        distance = instruction[1]
        if operation == 'N':
            self.y += distance
        elif operation == 'S':
            self.y -= distance

        elif operation == 'E':
            self.x += distance
        elif operation == 'W':
            self.x -= distance

        elif operation == 'F':
            self.move((self.facing, distance))

        elif operation == 'R':
            self.facing_index = self.calculate_turn(distance)
        elif operation == 'L':
            self.facing_index = self.calculate_turn(-distance)

    @property
    def location(self):
        return self.x, self.y

    @property
    def facing(self):
        return self.HEADINGS[self.facing_index]

    def calculate_turn(self, angle):
        offset = angle // 90
        return (self.facing_index + offset) % 4


if __name__ == "__main__":
    with open("input.txt", 'r') as input_file:
        values = [(instruction[0], int(instruction[1:])) for instruction in input_file.read().split("\n")]

    print(values)
    ship = Ship()
    for move in values:
        ship.move(move)

    print(f"Distance from starting location: {abs(ship.x) + abs(ship.y)}")
