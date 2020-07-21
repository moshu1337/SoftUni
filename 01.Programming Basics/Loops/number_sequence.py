import sys
numbers_count = int(input())
highest_number = -sys.maxsize
lowest_number = sys.maxsize
for counter in range(numbers_count):
    current_number = int(input())

    if current_number < lowest_number:
        lowest_number = current_number

    if current_number > highest_number:
        highest_number = current_number

print(f'Max number: {highest_number}')
print(f'Min number: {lowest_number}')