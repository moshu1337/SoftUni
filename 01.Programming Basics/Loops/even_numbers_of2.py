n = int(input())
value = 0
for number in range(n+1):
    if number % 2 == 0:
        value = 2 ** number
        print(value)