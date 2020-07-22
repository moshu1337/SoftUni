word = input()
reversed_word = ''
word_lenght = len(word)
for index in range(len(word) -1, -1, -1):
    reversed_word += word[index]

print(reversed_word)

for c in reversed(word):
    reversed_word += c