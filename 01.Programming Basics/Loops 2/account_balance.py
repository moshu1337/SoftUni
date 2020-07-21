number_of_deposits = int(input())
deposits_made = 0
deposit = 0
total_balance = 0

while deposits_made < number_of_deposits:
    deposit = float(input())
    if deposit > 0:
        print(f"Increase: {deposit:.2f}")
        total_balance += deposit
    else:
        print("Invalid operation!")
        break
    deposits_made += 1
print(f"Total: {total_balance:.2f}")

###
counter = int(input())
transactions_made = 0
transaction = 0
total_balance = 0
while transactions_made < counter:
    transaction = float(input())
    if transaction >= 0:
        print(f'Increase: {transaction:.2f}')
        total_balance += transaction
    else:
        print('Invalid operation!')
        break
    transactions_made += 1
print(f'Total: {total_balance:.2f}')
###