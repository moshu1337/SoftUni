budget = int(input())
season = input()
fishermen_total = int(input())
price = 0

if season == "Spring":
    price = 3000
elif season == "Summer" or season == "Autumn":
    price = 4200
elif season == "Winter":
    price = 2600

if fishermen_total <= 6:
    price = price - (price * 0.1)
elif fishermen_total <= 11:
    price = price - (price * 0.15)
else:
    price = price - (price * 0.25)

if fishermen_total % 2 == 0 and season != "Autumn":
    price = price * 0.95

if budget >= price:
    print(f"Yes! You have {budget - price:.2f} leva left.")
else:
    print(f"Not enough money! You need {price - budget:.2f} leva.")
