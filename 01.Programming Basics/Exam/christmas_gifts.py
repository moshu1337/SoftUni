number_of_adults = 0
number_of_kids = 0
money_for_toys = 0
money_for_sweaters = 0

while True:
    command = input()
    if command == "Christmas":
        break
    else:
        age = int(command)
    if age <= 16:
        number_of_kids += 1
    else:
        number_of_adults += 1

total_price_sweaters = number_of_adults * 15
total_price_toys = number_of_kids * 5


print(f"Number of adults: {number_of_adults}")
print(f"Number of kids: {number_of_kids}")
print(f"Money for toys: {total_price_toys}")
print(f"Money for sweaters: {total_price_sweaters}")