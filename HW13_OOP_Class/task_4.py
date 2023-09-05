class Robot:
    def __init__(self, orientation, position_x, position_y):
        self.orientation = orientation
        self.position_x = position_x
        self.position_y = position_y

    def move(self, steps):
        if self.orientation == "left":
            self.position_x -= steps
        elif self.orientation == "right":
            self.position_x += steps
        elif self.orientation == "up":
            self.position_y += steps
        elif self.orientation == "down":
            self.position_y -= steps

    def turn(self, direction):
        directions = ["up", "right", "down", "left"]
        if direction in directions:
            orientation_index = directions.index(self.orientation)
            if direction == "left":
                orientation_index = (orientation_index - 1) % len(directions)
            elif direction == "right":
                orientation_index = (orientation_index + 1) % len(directions)
            self.orientation = directions[orientation_index]

    def display_position(self):
        print(
            f"Position: ({self.position_x}, {self.position_y})",
            f"Orientation: {self.orientation}",
        )


robot = Robot("up", 0, 0)

robot.move(4)

robot.display_position()

robot.turn("right")

robot.move(1)

robot.display_position()
