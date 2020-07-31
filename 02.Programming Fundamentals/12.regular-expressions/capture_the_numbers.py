import re
pattern = r"\d+"

while True:
    text = input()

    if not text:
        break

    numbers = re.findall(pattern, text)
    for number in numbers:
        print(number, end=' ')
