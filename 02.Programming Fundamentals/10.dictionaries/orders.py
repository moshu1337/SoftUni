from collections import defaultdict
items_quantities = defaultdict(int)
items_prices = defaultdict(float)
items_bought = defaultdict(float)
while True:
    command = input()
    if command == 'buy':
        break
    tokens = command.split()
    product = tokens[0]
    price_of_product = float(tokens[1])
    quantity = int(tokens[2])
    if price_of_product != items_prices[product]:
        items_prices[product] = price_of_product
    items_quantities[product] += quantity
    items_bought[product] = items_prices[product] * items_quantities[product]


for key, value in items_bought.items():
    print(f'{key} -> {value:.2f}')
