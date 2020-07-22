lost_fights = int(input())

helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

trashed_helmet = 0
trashed_sword = 0
trashed_shield = 0
trashed_shield_counter = 0
armor_repair_needs = 0
for lost_game in range(1, lost_fights + 1):
    if lost_game % 2 == 0:
        trashed_helmet += 1
    if lost_game % 3 == 0:
        trashed_sword += 1
        if lost_game % 2 == 0:
            trashed_shield += 1
            trashed_shield_counter += 1
    if trashed_shield_counter % 2 == 0 and trashed_shield_counter >= 1:
        armor_repair_needs += 1
        trashed_shield_counter = 0


helmet_repair_price = helmet_price * trashed_helmet
sword_repair_price = sword_price * trashed_sword
shield_repair_price = shield_price * trashed_shield
armor_repair_price = armor_price * armor_repair_needs

total_expenses = helmet_repair_price + sword_repair_price + shield_repair_price + armor_repair_price

print(f'Gladiator expenses: {total_expenses:.2f} aureus')
