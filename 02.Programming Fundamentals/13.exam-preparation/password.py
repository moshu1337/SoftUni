import re
n = int(input())
pattern = r"^(.+)>(\d{3})\|([a-z]{3})\|([A-Z]{3})\|([^<>]{3})<(\1)$"

for _ in range(n):
    password = input()

    match = re.fullmatch(pattern, password)

    if match is None:
        print("Try another password!")
        continue

    print(f"Password: {match[2]}{match[3]}{match[4]}{match[5]}")

