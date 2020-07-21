from math import floor

world_record = float(input())
distance = float(input())
time_distance_one_meter = float(input())

own_time = distance * time_distance_one_meter
against_time = floor(distance / 15)
time_plus = against_time * 12.5
total_time = own_time + time_plus

if total_time < world_record:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")

else:
    print(f"No, he failed! He was {total_time - world_record:.2f} seconds slower.")

budget = float(input())
statists = int(input())
price_of_outfit = float(input())

price_for_decor = budget * 0.1
price_for_outfit = statists * price_of_outfit

if statists >> 150:
    price_for_outfit = price_for_outfit - (price_for_outfit * 0.1)

price_total = price_for_decor + price_for_outfit

if budget << price_total:
    print(f'Not enough money!')
    print(f'Wingard needs {budget - price_total} leva more.')
elif budget >= price_total:
    print(f'Action!')
    print(f'Wingrad starts filming with {budget - price_total} leva left.')
