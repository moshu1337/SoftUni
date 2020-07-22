change = int(float(input()) * 100)
coins = 0

if change // 200 >= 1:
    coins += change // 200
    change -= 200 * change // 200
if change // 100 >= 1:
    coins += change // 100
    change -= 100 * change // 100
if change // 50 >= 1:
    coins += change // 50
    change -= 50 * change // 50

