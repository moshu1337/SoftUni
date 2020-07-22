cards = input().split()
cards = set(cards)
team_a = []
team_b = []
for card in cards:
    if card[0] == "A":
        team_a.append(card)
    elif card[0] == "B":
        team_b.append(card)

print(f"Team A - {11 - len(team_a)}; Team B - {11 - len(team_b)}")
if 11 - len(team_a) < 7 or 11 - len(team_b) < 7:
    print("Game was terminated")
