factor = int(input())
factor_saved = factor
count = int(input())
numbers = []

for _ in range(count):
    numbers.append(factor)
    factor += factor_saved

print(numbers)
