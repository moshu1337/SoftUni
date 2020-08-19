import re
pattern = r"(=|\/)([A-Z][a-z]{2,})\1"
string = input()
destinations = []
travel_points = 0

match = re.findall(pattern, string)

for m in match:
    destinations.append(m[1])

for dest in destinations:
    travel_points += len(dest)

print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {travel_points}")
