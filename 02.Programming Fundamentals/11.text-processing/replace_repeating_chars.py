text = input()

for i in range(len(text)):
    char = text[i]
    if i + 1 == len(text) or char != text[i + 1]:
        print(char, end="")

