from math import cos, sin, radians


class Ship:
    def __init__(self):
        self.x = 0
        self.y = 0

        self.waypoint_x = 10
        self.waypoint_y = 1

    def move(self, instruction):
        operation = instruction[0]
        arg = instruction[1]

        if operation == 'N':
            self.waypoint_y += arg
        elif operation == 'S':
            self.waypoint_y -= arg

        elif operation == 'E':
            self.waypoint_x += arg
        elif operation == 'W':
            self.waypoint_x -= arg

        elif operation == 'F':
            for _ in range(arg):
                self.x += self.waypoint_x
                self.y += self.waypoint_y

        elif operation == 'R':
            self.turn(arg)
        elif operation == 'L':
            self.turn(-arg)

    @property
    def location(self):
        return self.x, self.y

    @property
    def waypoint(self):
        return self.waypoint_x, self.waypoint_y

    def turn(self, angle):
        rad_angle = radians(angle)  # Converts the angle to radians and inverts it because we are rotating count-clockwise.

        new_x = self.waypoint_x * round(cos(rad_angle)) + self.waypoint_y * round(sin(rad_angle))
        new_y = -self.waypoint_x * round(sin(rad_angle)) + self.waypoint_y * round(cos(rad_angle))

        self.waypoint_x = new_x
        self.waypoint_y = new_y


if __name__ == "__main__":
    with open("input.txt", 'r') as input_file:
        values = [(instruction[0], int(instruction[1:])) for instruction in input_file.read().split("\n")]

    print(values)
    ship = Ship()
    for move in values:
        ship.move(move)

    print(f"Distance from starting location: {abs(ship.x) + abs(ship.y)}")
