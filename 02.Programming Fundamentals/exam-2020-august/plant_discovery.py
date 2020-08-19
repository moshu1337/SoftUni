n = int(input())

rarities = {}
ratings = {}

for i in range(n):
    data = input().split("<->")
    plant = data[0]
    rarity = int(data[1])

    if plant not in rarities:
        rarities[plant] = rarity
        ratings[plant] = []
    else:
        rarities[plant] = rarity

cmd_input = input()

while cmd_input != "Exhibition":
    command = cmd_input.split(': ')[0]
    plant_info = cmd_input.split(": ")[1]
    plant = plant_info.split(" - ")[0]

    if command == "Rate":
        if plant in rarities:
            rating = float(plant_info.split(" - ")[1])
            ratings[plant].append(rating)

    elif command == "Update":
        if plant in rarities:
            new_rarity = int(plant_info.split(" - ")[1])
            rarities[plant] = new_rarity
    elif command == "Reset":
        if plant in ratings:
            del ratings[plant]
            ratings[plant] = [0.0]

    cmd_input = input()


sorted_rarities = dict(sorted(rarities.items(), key=lambda x: -x[1]))

for key, item in ratings.items():
    ratings[key] = sum(item) / len(item)

print(ratings)
print(sorted_rarities)

values = ratings.value

print("Plants for the exhibition:")
for k, v in sorted_rarities.items():
    print(f"- {k}; Rarity: {v}; Rating: {ratings[k]:.2f}")

