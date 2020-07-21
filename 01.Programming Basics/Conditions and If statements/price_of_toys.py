price_needed = float(input())
puzzles_count = int(input())
dolls_count = int(input())
bears_count = int(input())
minions_count = int(input())
trucks_count = int(input())

money_made = puzzles_count * 2.60 + dolls_count * 3 + bears_count * 4.10 + minions_count * 8.20 + trucks_count * 2
toys_count = puzzles_count + dolls_count + bears_count + minions_count + trucks_count
if toys_count >= 50:
    money_made *= 0.75
money_made *= 0.9

if money_made >= price_needed:
    print(f'Yes! {money_made - price_needed:.2f} lv left.')
else:
    print(f'Not enough money! {price_needed - money_made:.2f} lv needed.')
