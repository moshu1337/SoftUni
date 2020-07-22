n = int(input())
CAPACITY = 255
total_quantities = 0

for _ in range(1, n + 1):
    quantities = int(input())
    if total_quantities + quantities > CAPACITY:
        print('Insufficient capacity!')
    else:
        total_quantities += quantities

print(total_quantities)
