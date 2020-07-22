def perfect_num(num):
    divisors_list = []
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            divisors_list.append(i)
    if sum(divisors_list) == num:
        print('We have a perfect number!')
    else:
        print('It\'s not so perfect.')


num = int(input())
perfect_num(num)
