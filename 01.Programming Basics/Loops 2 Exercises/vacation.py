price_for_excursion = float(input())
saved = float(input())
total_days = 1
spending_days = 0

while True:
    command = input()
    spent_saved = float(input())
    if command == 'save':
        saved += spent_saved
        spending_days = 0
        if saved >= price_for_excursion:
            print(f"You saved the money for {total_days} days.")
            break
    elif command == 'spend':
        saved -= spent_saved
        spending_days += 1
        if spending_days == 5:
            print("You can't save the money.")
            print(f"{total_days}")
            break
        if saved < 0:
            saved = 0
    total_days += 1
