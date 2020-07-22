def order_to_get(piece: str, quantity: int):
    if piece == 'coffee':
        return 1.50 * quantity  # it will be good to make constants like COFFEE_PRICE = 1.50 (outside def)
    if piece == 'water':
        return 1.00 * quantity
    if piece == 'coke':
        return 1.40 * quantity
    if piece == 'snacks':
        return 2 * quantity


order_type: str = input()
quantity_of_order: int = int(input())
print(f'{order_to_get(order_type, quantity_of_order):.2f}')
