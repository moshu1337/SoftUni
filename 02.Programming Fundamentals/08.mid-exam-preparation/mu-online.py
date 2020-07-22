initial_health = 100
initial_bitcoin = 0
dungeon_rooms = input().split("|")
is_alive = True

for i in range(len(dungeon_rooms)):
    room = dungeon_rooms[i]

    tokens = room.split()
    encounter = tokens[0]
    amount = int(tokens[1])

    if encounter == "potion":
        temp_health = initial_health
        initial_health += amount
        healed = amount

        if initial_health > 100:
            initial_health = 100
            healed = 100 - temp_health
        print(f"You healed for {healed} hp.")
        print(f"Current health: {initial_health} hp.")

    elif encounter == "chest":
        initial_bitcoin += amount
        print(f"You found {amount} bitcoins.")
    else:
        initial_health -= amount

        if initial_health > 0:
            print(f"You slayed {encounter}.")
        else:
            print(f"You died! Killed by {encounter}.")
            print(f"Best room: {i + 1}")
            is_alive = False
            break

if is_alive:
    print(f"You've made it!\nBitcoins: {initial_bitcoin}\nHealth: {initial_health}")
