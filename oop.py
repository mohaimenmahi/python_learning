class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print(f'Move {self.x} horizontally, {self.y} vertically')

    def draw(self):
        print(f"Draw a line with point ({self.x},{self.y})")


point1 = Point(15, 11)

print(point1.x)

point1.draw()

