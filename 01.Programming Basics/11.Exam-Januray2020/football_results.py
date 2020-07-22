total_lost = 0
total_won = 0
drawn_games = 0

for i in range (1, 4):
    left, right = input().split(":")
    if left > right:
        total_won += 1
    elif right > left:
        total_lost += 1
    else:
        drawn_games += 1

print(f'Team won {total_won} games.')
print(f'Team lost {total_lost} games.')
print(f'Drawn games: {drawn_games}')