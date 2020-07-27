from collections import defaultdict
text = input()

occurrences = defaultdict(int)

for char in text:
    if char == " ":
        continue
    occurrences[char] += 1

for key, value in occurrences.items():
    print(f"{key} -> {value}")
