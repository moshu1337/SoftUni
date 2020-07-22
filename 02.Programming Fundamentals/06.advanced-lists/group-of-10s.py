import math

list_of_numbers = list(map(int, input().split(', ')))
max_nums = max(list_of_numbers)
number_of_groups = math.ceil(max_nums / 10)

for i in range(1, number_of_groups + 1):
    upper = i * 10
    lower = upper - 10

    current_range = [n for n in list_of_numbers if lower < n <= upper]

    print(f"Group of {i * 10}'s: {current_range}")
