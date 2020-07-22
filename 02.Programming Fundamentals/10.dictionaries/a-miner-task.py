# from collections import defaultdict
# resources = defaultdict(int)
resources = {}
while True:
    command = input()
    if command == 'stop':
        break
    value = int(input())
    if command not in resources:
        resources[command] = 0
    resources[command] += value

for key, value in resources.items():
    print(f'{key} -> {value}')

# can also do it with defaultdict whithout the if statement on line 9
