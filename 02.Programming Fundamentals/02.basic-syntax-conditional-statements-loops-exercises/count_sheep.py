sheep = int(input())

for count in range(1, sheep + 1):
    print(f'{count} sheep...', end='', sep='')
    sheep -= 1