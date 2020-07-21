target = 10000
total_steps = 0
while total_steps < target:
    command = input()
    if command == "Going home":
        steps_to_home = int(input())
        total_steps += steps_to_home
        break
    else:
        steps = int(command)
        total_steps += steps
if total_steps >= target:
    print("Goal reached! Good job!")
else:
    print(f"{target - total_steps} more steps to reach goal.")


