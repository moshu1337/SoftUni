command = input()
words = []
while command != 'end':
    words.append(command)
    command = input()

for word in words:
    print(f"{word} = {word[::-1]}")


def reverse(string):
    s = ""
    for char in reversed(string):
        s += char

# can do with function or slicing
