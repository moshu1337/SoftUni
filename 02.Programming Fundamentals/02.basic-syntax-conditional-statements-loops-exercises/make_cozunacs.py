budget = float(input())
price_of_1kg_flour = float(input())

price_of_1pack_eggs = price_of_1kg_flour * 0.75
price_of_1liter_milk = price_of_1kg_flour * 1.25
milk_250ml = price_of_1liter_milk / 4
cozunac_price = milk_250ml + price_of_1kg_flour + price_of_1pack_eggs
cozunacs_made = 0
colored_eggs = 0

while budget >= cozunac_price:
    cozunacs_made += 1
    colored_eggs += 3
    if cozunacs_made % 3 == 0:
        colored_eggs -= cozunacs_made - 2
    budget -= cozunac_price

print(f"You made {cozunacs_made} cozonacs! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")