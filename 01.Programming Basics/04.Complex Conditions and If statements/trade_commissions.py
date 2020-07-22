city = input().lower()
volume_of_sales = float(input())
commission = 0.00

if city == 'sofia' and 0 <= volume_of_sales <= 500:
    commission = 0.05
elif city == 'sofia' and 500 < volume_of_sales <= 1000:
    commission = 0.07
elif city == 'sofia' and 1000 < volume_of_sales <= 10000:
    commission = 0.08
elif city == 'sofia' and volume_of_sales > 10000:
    commission = 0.12

if city == 'varna' and 0 <= volume_of_sales <= 500:
    commission = 0.045
elif city == 'varna' and 500 < volume_of_sales <= 1000:
    commission = 0.075
elif city == 'varna' and 1000 < volume_of_sales <= 10000:
    commission = 0.10
elif city == 'varna' and volume_of_sales > 10000:
    commission = 0.13

if city == 'plovdiv' and 0 <= volume_of_sales <= 500:
    commission = 0.055
elif city == 'plovdiv' and 500 < volume_of_sales <= 1000:
    commission = 0.08
elif city == 'plovdiv' and 1000 < volume_of_sales <= 10000:
    commission = 0.12
elif city == 'plovdiv' and volume_of_sales > 10000:
    commission = 0.145

if commission > 0:
    result = commission * volume_of_sales
    print(f'{result:.2f}')
else:
    print('error')
