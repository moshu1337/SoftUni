class Robot:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def introduce_self(self):
        return f"Hello, I'm {self.name}, I'm {self.color} and I weight {self.weight}"


number_of_robots = int(input())
for _ in range(number_of_robots):
    name, color, weight = input().split()
    robot = Robot(name, color, weight)
    print(robot.introduce_self())


