from collections import defaultdict

number_of_commands = int(input())
registered = defaultdict(str)

for operation in range(number_of_commands):
    args = input().split(' ')
    command = args[0]
    username = args[1]

    if command == 'register':
        license_plate = args[2]
        if username in registered:
            print(f"ERROR: already registered with plate number {license_plate}")
            continue
        registered[username] += license_plate
        print(f"{username} registered {license_plate} successfully")
    elif command == 'unregister':
        if username not in registered:
            print(f"ERROR: user {username} not found")
            continue
        registered.pop(username)
        print(f"{username} unregistered successfully")

for key, value in registered.items():
    print(f"{key} => {value}")