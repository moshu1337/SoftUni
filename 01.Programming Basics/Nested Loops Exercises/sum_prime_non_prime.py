sum_primes = 0
sum_nonprimes = 0

while True:
    command = input()
    if command == "stop":
        break
    number = int(command)
    if number < 0:
        print("Number is negative.")
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break
    if is_prime:
        sum_primes += number
    else:
        sum_nonprimes += number

print(f"Sum of all prime numbers is: {sum_primes}")
print(f"Sum of all non prime numbers is: {sum_nonprimes}")
