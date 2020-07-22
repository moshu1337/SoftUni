data = input().split(' ')
inventory = {
    data[index]: int(data[index + 1])
    for index in range(0, len(data), 2)
}

products_check = input().split(' ')

for searched_product in products_check:
    if searched_product in inventory:
        quantity = inventory[searched_product]
        print(f"We have {quantity} of {searched_product} left")
    else:
        print(f"Sorry, we don't have {searched_product}")

