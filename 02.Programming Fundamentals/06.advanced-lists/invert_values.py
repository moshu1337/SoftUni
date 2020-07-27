numbers = input()
nums_str = numbers.split()
inverted = []

for number in nums_str:
    number_inverted = -int(number)
    inverted.append(number_inverted)

print(inverted)

