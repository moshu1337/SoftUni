n = int(input())
trains = [0] * n

while True:
    command = input()
    if command == 'End':
        break

    token = command.split(' ')
    command = token[0]
    if command == 'add':
        people_to_add = int(token[1])
        trains[-1] += people_to_add
    elif command == 'insert':
        wagon = int(token[1])
        people_to_insert = int(token[2])
        trains[wagon] += people_to_insert
    elif command == 'leave':
        wagon = int(token[1])
        people_to_remove = int(token[2])
        trains[wagon] -= people_to_remove

print(trains)