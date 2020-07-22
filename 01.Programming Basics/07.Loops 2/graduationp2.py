name = input()
counter = 1
total_grade = 0
skusan = 0
while counter <= 12:
    curr_grade = float(input())
    if curr_grade >= 4:
        total_grade += curr_grade
        counter += 1
    else:
        skusan += 1
    if skusan > 1:
        print(f"{name} has been excluded at {counter} grade")
        break

average = total_grade / 12
if skusan <= 1:
    print(f"{name} graduated. Average grade: {average:.2f}")



name = input()
counter = 1
total_grade = 0
skusan = 0
is_expelled = False
while counter <= 12:
    curr_grade = float(input())
    if curr_grade >= 4:
        total_grade += curr_grade
        counter += 1
    else:
        skusan += 1
    if skusan == 2:
        is_expelled =True
        print(f"{name} has been excluded at {counter} grade")
        break

if not is_expelled:
    average = total_grade / 12
    print(f"{name} graduated. Average grade: {average:.2f}")

