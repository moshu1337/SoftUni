def ascii_char(word):
    temp = ''
    for char in word:
        if not str(char).isdigit():
            break
        temp += char
    ascii_value = int(temp)
    char_value = chr(ascii_value)
    new_word = word.replace(temp, char_value)
    return new_word


def replace_second_and_last(word):
    temp = list(word)
    temp[1], temp[-1] = temp[-1], temp[1]
    return ''.join(temp)


def decrypt(word):
    res = ascii_char(word)
    res = replace_second_and_last(res)
    return res


secret_message = input().split()

for word in secret_message:
    print(decrypt(word), end=' ')