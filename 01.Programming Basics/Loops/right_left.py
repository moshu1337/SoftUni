n = int(input())

left_sum = 0
right_sum = 0

for nums in range(n * 2):
    num = int(input())
    if nums < n:
        left_sum += num
    else:
        right_sum += num

if left_sum == right_sum:
    print(f'Yes, sum = {left_sum}')
else:
    print(f'No, diff = {abs(left_sum - right_sum)}')

