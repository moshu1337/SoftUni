def odd_even_sum(number):
    odd_sum = 0
    even_sum = 0
    res = [int(x) for x in str(number)]
    for num in res:
        if num % 2:
            odd_sum += num
        else:
            even_sum += num
    return f'Odd sum = {odd_sum}, Even sum = {even_sum}'


a = int(input())

print(odd_even_sum(a))

# or
# def even_and_odd_sum(num):
#     num = str(num)
#     even_digits_sum = 0
#     odd_digits_sum = 0
#     for i in num:
#         i = int(i)
#         if i % 2 == 0:
#             even_digits_sum += i
#         else:
#             odd_digits_sum += i
#     return f'Odd sum = {odd_digits_sum}, Even sum = {even_digits_sum}'
# n = int(input())
# print(even_and_odd_sum(n))