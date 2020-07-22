data = input()
products = data.split(" ")

inventory = {}

for index in range(0, len(products), 2):
    product_name = products[index]
    product_quantity = products[index + 1]
    inventory[product_name] = int(product_quantity)
