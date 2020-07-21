n = int(input())
p1 = 0
p2 = 0
p3 = 0

for _ in range(n):
    number = int(input())
    if number % 2 == 0:
        p1 += 1
    if number % 3 == 0:
        p2 += 1
    if number % 4 == 0:
        p3 += 1
    else:
        pass

precentofp1 = p1 / n * 100
precentofp2 = p2 / n * 100
precentofp3 = p3 / n * 100

print(f"{precentofp1:.2f}%")
print(f"{precentofp2:.2f}%")
print(f"{precentofp3:.2f}%")