import math

count_of_students = int(input())
count_of_lectures = int(input())
additional_bonus = int(input())
most_attendances = 0
max_bonus = 0


for _ in range(count_of_students):
    student_attendances = int(input())
    student_bonus = student_attendances / count_of_lectures * (5 + additional_bonus)
    if student_bonus > max_bonus:
        max_bonus = student_bonus
        most_attendances = student_attendances
    # if student_attendances > most_attendances:
    #     most_attendances = student_attendances


# max_bonus = most_attendances / count_of_lectures * (5 + additional_bonus)

print(f"Max Bonus: {math.ceil(max_bonus)}.")
print(f"The student has attended {most_attendances} lectures.")

# student bonus must be done in for loop to cover all chances
