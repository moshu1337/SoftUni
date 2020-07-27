numbers_string = input().split(', ')
numbers = []
beggarscount = int(input())

for num_str in numbers_string:
    number = int(num_str)
    numbers.append(number)

beggars = []

for _ in range(beggarscount):
    beggars.append(0)

index = 0

for number in numbers:
    beggars[index] += number
    index += 1

    if index == beggarscount:
        index = 0

print(beggars)
