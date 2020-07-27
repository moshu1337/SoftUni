text = input()
total_power = 0
i = 0

while i < len(text):
    char = text[i]
    if char == '>':
        power = int(text[i + 1])
        total_power += power
    else:
        if total_power > 0:
            text = text[:i] + text[i + 1:]
            total_power -= 1
            i -= 1
    i += 1

print(text)
