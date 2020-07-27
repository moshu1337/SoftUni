words = input().split(' ')
repeated = []

for word in words:
    for letter in word:
        repeated.append(word)

print(''.join(repeated))


def repeat_by_length(word):
    return word * len(word)

# can also do it more automated with function (reminder to use functions more)
