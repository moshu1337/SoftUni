n1 = int(input())
n2 = int(input())

for number in range(n1, n2 + 1):
    number_to_str = str(number)
    even_sum = 0
    odd_sum = 0
    for index, digit in enumerate(number_to_str):
        if index % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)

    if even_sum == odd_sum:
        print(number, end=' ')
