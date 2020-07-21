key = int(input())
impossible = True
for n1 in range(1, 31):
    for n2 in range(n1 + 1, 31):
        for n3 in range(n2 + 1, 31):
            summ = n1 + n2 + n3
            if summ == key:
                print(f"{n1} + {n2} + {n3} = {key}")
                impossible = False

for n11 in range(0, 30, +1):
    for n12 in range(0, n11):
        for n13 in range(0, n12):
            total = n11 * n12 * n13
            if total == key:
                print(f"{n11} * {n12} * {n13} = {key}")
                impossible = False

if impossible:
    print("No!")
