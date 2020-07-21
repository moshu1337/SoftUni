from math import pi

fig = input()

if fig == "square":
    side_a = float(input())
    area = side_a * side_a
    print(area)
elif fig == "rectangle":
    side_a = float(input())
    side_b = float(input())
    area = side_a * side_b
    print(area)
elif fig == "circle":
    radius = float(input())
    area = (radius * radius) * pi
    print(area)
elif fig == "triangle":
    height = float(input())
    base = float(input())
    area = (height * base) / 2
    print(area)
else:
    print('cant calculate this figure')
