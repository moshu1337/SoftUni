key = int(input())
impossible = True
for n1 in range(1, 31):
    for n2 in range(n1 + 1, 31):
        for n3 in range(n2 + 1, 31):
            summ = n1 + n2 + n3
            total = n1 * n2 * n3
            if total == key:
                print(f"{n1} * {n2} * {n3} = {key}")
            if summ == key:
                print(f"{n1} + {n2} + {n3} = {key}")
