def only_digits(string):
    digits = ''
    for char in text:
        if char.isdigit():
            digits += char
    return digits


def only_letters(string):
    letters = ''
    for char in text:
        if char.isalpha():
            letters += char
    return letters


def only_others(string):
    others = ''
    for char in text:
        if not char.isdigit() and not char.isalpha():
            others += char
    return others


text = input()

print(only_digits(text))
print(only_letters(text))
print(only_others(text))
