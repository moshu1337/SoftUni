emoticon = ':'
text = input()


for char in range(len(text)):
    if text[char] == emoticon:
        if text[char + 1] != " ":
            print(f":{text[char + 1]}")

            