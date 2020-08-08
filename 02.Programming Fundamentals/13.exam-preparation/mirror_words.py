import re
regex = r"(@|#)([A-Za-z]{3,})\1\1([A-Za-z]{3,})\1"
data = input()
mirror_words = []
matches = re.findall(regex, data)

for match in matches:
    first = match[1]
    second = match[2]
    if first == second[::-1]:
        mirror_words.append(first + " <=> " + second)

if len(matches) == 0:
    print("No word pairs found!")
else:
    print(f"{len(matches)} word pairs found!")

if len(mirror_words) == 0:
    print("No mirror words!")
else:
    print(f"The mirror words are:")
    print(', '.join(mirror_words))