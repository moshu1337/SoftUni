type_of_flower = input()
total_flowers = int(input())
budget = int(input())
price = 0

rose = 5
dahlias = 3.80
tulips = 2.80
narcissus = 3
gladiolus = 2.5

if type_of_flower == "Roses":
    price = total_flowers * rose
elif type_of_flower == "Dahlias":
    price = total_flowers * dahlias
elif type_of_flower == "Tulips":
    price = total_flowers * tulips
elif type_of_flower == "Narcissus":
    price = total_flowers * narcissus
elif type_of_flower == "Gladiolus":
    price = total_flowers * gladiolus

if type_of_flower == "Roses" and total_flowers > 80:
    price = price * 0.9
elif type_of_flower == "Dahlias" and total_flowers > 90:
    price = price * 0.85
elif type_of_flower == "Tulips" and total_flowers > 80:
    price = price * 0.85
elif type_of_flower == "Narcissus" and total_flowers < 120:
    price = price * 1.15
elif type_of_flower == "Gladiolus" and total_flowers < 80:
    price = price * 1.2

money_left = budget - price
money_needed = price - budget

if budget >= price:
    print(f"Hey, you have a great garden with {total_flowers} {type_of_flower} and {money_left:.2f} leva left.")
else:
    print(f"Not enough money, you need {money_needed:.2f} leva more.")
