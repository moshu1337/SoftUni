month = input()
spent_hours_total = int(input())
total_people_in_group = int(input())
time_of_day = input()
price = 0

if month == "march" or month == "april" or month == "may":
    if time_of_day == "day":
        price = 10.50
    elif time_of_day == "night":
        price = 8.4

if month == "june" or month == "july" or month == "august":
    if time_of_day == "day":
        price = 12.60
    elif time_of_day == "night":
        price = 10.20

if total_people_in_group >= 4:
    price = price - (price * 0.1)
else:
    pass

if spent_hours_total >= 5:
    price = price - (price * 0.5)
else:
    pass

total_price = (price * total_people_in_group) * spent_hours_total

print(f"Price per person for one hour: {price:.2f}")
print(f"Total cost of the visit: {total_price:.2f}")




month = input()
hours = int(input())
group = int(input())
time_of_day = input()
cost_per_person = 0
total_cost = 0
if time_of_day == "day":
    if month == "march" or month == "april" or month == "may":
        cost_per_person = 10.50
    else:
        cost_per_person = 12.60
elif time_of_day == "night":
    if month == "march" or month == "april" or month == "may":
        cost_per_person = 8.40
    else:
        cost_per_person = 10.20
if group >= 4:
    cost_per_person = cost_per_person * 0.90
if hours >= 5:
    cost_per_person = cost_per_person * 0.50
total_cost = cost_per_person * hours * group
print(f"Price per person for one hour: {cost_per_person:.2f}")
print(f"Total cost of the visit: {total_cost:.2f}")