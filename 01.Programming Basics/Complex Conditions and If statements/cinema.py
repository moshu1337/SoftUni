screening_type = input()
rows = int(input())
columns = int(input())
all_places = rows * columns
price_of_tickets = 0
if screening_type == 'Premiere':
    price_of_tickets = all_places * 12.00
elif screening_type == 'Normal':
    price_of_tickets = all_places * 7.50
elif screening_type == 'Discount':
    price_of_tickets = all_places * 5.00

print(f'{price_of_tickets:.2f} leva')