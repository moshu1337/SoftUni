numbers = list(map(int, input().split()))
average = sum(numbers) / len(numbers)
greater_than_average = []
is_average = False
for number in numbers:
    if number > average:
        greater_than_average.append(number)
        is_average = True


greater_than_average.sort(reverse=True)
while len(greater_than_average) > 5:
    del greater_than_average[-1]


if is_average is False:
    print('No')
else:
    greater_than_average.sort(reverse=True)
    top5 = list(map(str, greater_than_average))
    print(' '.join(top5))

