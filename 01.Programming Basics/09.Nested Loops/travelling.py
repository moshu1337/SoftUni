command = input()
while command != "End":
    minimal_budget = float(input())
    saved_money = 0
    while saved_money < minimal_budget:
        saving = float(input())
        saved_money += saving
        if saved_money >= minimal_budget:
            print(f"Going to {command}!")
            break
    command = input()
    if command == "End":
        break

