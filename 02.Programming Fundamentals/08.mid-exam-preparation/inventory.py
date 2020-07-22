collecting_items = input().split(', ')
command = input()

while command != "Craft!":
    arguments = command.split(" - ")
    first_argument = arguments[0]
    second_argument = arguments[1]

    if first_argument == "Collect":
        if second_argument not in collecting_items:
            collecting_items.append(second_argument)

    elif first_argument == "Drop":
        if second_argument in collecting_items:
            collecting_items.remove(second_argument)

    elif first_argument == "Combine Items":
        items = second_argument.split(":")
        old_item = items[0]
        new_item = items[1]
        if old_item in collecting_items:
            index_to_append = collecting_items.index(old_item) + 1
            collecting_items.insert(index_to_append, new_item)

    elif first_argument == "Renew":
        if second_argument in collecting_items:
            collecting_items.append(collecting_items.pop(collecting_items.index(second_argument)))
    command = input()

print(", ".join(collecting_items))
