total_electrons = int(input())
res = []
shield_index = 1

while total_electrons > 0:
    value = 2 * shield_index ** 2
    if value > total_electrons:
        value = total_electrons

    res.append(value)
    total_electrons -= value
    shield_index += 1

print(res)
