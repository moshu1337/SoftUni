username_wanted = input()

command = input()

while command != "Sign up":
    tokens = command.split(" ")
    to_do = tokens[0]
    if to_do == "Case":
        l_or_w = tokens[1]
        if l_or_w == "lower":
            username_wanted = username_wanted.lower()
            print(username_wanted)
        else:
            username_wanted = username_wanted.upper()
            print(username_wanted)

    elif to_do == "Reverse":
        start_index = int(tokens[1])
        end_index = int(tokens[2])
        length = len(username_wanted)

        if start_index < 0 or start_index >= length or end_index < 0 or end_index >= length:
            command = input()
            continue

        res = username_wanted[start_index:end_index + 1]
        reversed_res = res[::-1]
        print(reversed_res)
    elif to_do == "Cut":
        substring = tokens[1]
        if substring in username_wanted:
            username_wanted = username_wanted.replace(substring, '')
            print(username_wanted)
        else:
            print(f"The word {username_wanted} doesn't contain {substring}.")

    elif to_do == "Replace":
        char = tokens[1]
        if char in username_wanted:
            username_wanted = username_wanted.replace(char, '*')
            print(username_wanted)
        else:
            command = input()
            continue

    elif to_do == "Check":
        char = tokens[1]
        if char in username_wanted:
            print("Valid")
        else:
            print(f"Your username must contain {char}.")
    command = input()
