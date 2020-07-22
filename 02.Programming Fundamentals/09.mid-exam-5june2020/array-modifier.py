number_array = input().split()
commands = input()
while commands != "end":
    arguments = commands.split()
    command = arguments[0]

    if command == "swap":
        first_index = int(arguments[1])
        second_index = int(arguments[2])
        number_array[first_index], number_array[second_index] = number_array[second_index], number_array[first_index]

    elif command == "multiply":
        first_index = int(arguments[1])
        second_index = int(arguments[2])
        num1 = int(number_array[first_index])
        num2 = int(number_array[second_index])
        num1 *= num2
        number_array[first_index] = num1

    elif command == "decrease":
        number_array = [int(x) - 1 for x in number_array]

    commands = input()

number_array = list(map(str, number_array))
print(", ".join(number_array))
