MIN_NUMBER = 1
MAX_NUMBER = 100


while True:
    n = float(input())
    if MIN_NUMBER <= n <= MAX_NUMBER:
        print(f'The number {n} is between {MIN_NUMBER} and {MAX_NUMBER}')
        break

