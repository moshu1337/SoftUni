string = input()
cmd_input = input()
while cmd_input != "Travel":
    tokens = cmd_input.split(":")
    command = tokens[0]
    if command == "Add Stop":
        index = int(tokens[1])
        length = len(string)

        if index < 0 or index >= length:
            continue
        else:
            insertion = (tokens[2])
            string = string[:index] + insertion + string[index:]
            print(string)
    elif command == "Remove Stop":
        start_index = int(tokens[1])
        end_index = int(tokens[2])
        length = len(string)
        if start_index < 0 or start_index >= length or end_index < 0 or end_index >= length:
            continue
        else:
            string_to_remove = string[start_index:end_index + 1]
            string = string.replace(string_to_remove, "")
            print(string)
    elif command == "Switch":
        old_string = tokens[1]
        if old_string in string:
            new_string = tokens[2]
            string = string.replace(old_string, new_string)
            print(string)
    cmd_input = input()
print(f"Ready for world tour! Planned stops: {string}")

