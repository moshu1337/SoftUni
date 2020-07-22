name = input()
counter = 1
total_grade = 0
while counter <= 12:
    curr_grade = float(input())
    if curr_grade >= 4:
        total_grade += curr_grade
        counter += 1

average = total_grade / 12

print(f"{name} graduated. Average grade: {average:.2f}")
