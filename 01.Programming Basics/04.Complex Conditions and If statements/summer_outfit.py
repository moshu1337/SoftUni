weather = int(input())
time_of_the_day = input()
outfit = ''
shoes = ''
if time_of_the_day == 'Morning':
    if 10 <= weather <= 18:
        outfit = 'Sweatshirt'
        shoes = 'Sneakers'
    elif 18 < weather <= 24:
        outfit = 'Shirt'
        shoes = "Moccasins"
    else:
        outfit = 'T-Shirt'
        shoes = 'Sandals'

elif time_of_the_day == 'Afternoon':
    if 10 <= weather <= 18:
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif 18 < weather <= 24:
        outfit = 'T-Shirt'
        shoes = 'Sandals'
    else:
        outfit = 'Swim Suit'
        shoes = 'Barefoot'

else:
    outfit = 'Shirt'
    shoes = 'Moccasins'

print(f"It's {weather} degrees, get your {outfit} and {shoes}.")
