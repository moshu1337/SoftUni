n = int(input())
p1 = 0.00
p2 = 0.00
p3 = 0.00
p4 = 0.00
p5 = 0.00
for _ in range(n):
    number = int(input())
    if number < 200:
        p1 += 1.00
    elif 200 <= number <= 399:
        p2 += 1.00
    elif 400 <= number <= 599:
        p3 += 1.00
    elif 600 <= number <= 799:
        p4 += 1.00
    elif number >= 800:
        p5 += 1.00

precentofp1 = p1 / n * 100
precentofp2 = p2 / n * 100
precentofp3 = p3 / n * 100
precentofp4 = p4 / n * 100
precentofp5 = p5 / n * 100

print(f"{precentofp1:.2f}%")
print(f"{precentofp2:.2f}%")
print(f"{precentofp3:.2f}%")
print(f"{precentofp4:.2f}%")
print(f"{precentofp5:.2f}%")
