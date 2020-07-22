def chars_in_range(a, b):
    first_char = ord(a) + 1
    second_char = ord(b)
    result = ''
    for char in range(first_char, second_char):
        result += chr(char) + ' '
    return result

a = input()
b = input()
print(chars_in_range(a, b))
