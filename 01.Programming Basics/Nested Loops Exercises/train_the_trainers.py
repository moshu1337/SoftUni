djuri = int(input())
grade_sum = 0
counter = 0
while True:
    command = input()
    if command == "Finish":
        break
    presentation = command
    current_grade_sum = 0
    for i in range(djuri):
        grade = float(input())
        current_grade_sum += grade
        grade_sum += grade
        counter += 1
    average_grade = current_grade_sum / djuri
    print(f"{presentation} - {average_grade:.2f}.")

average = grade_sum / counter
print(f"Student's final assessment is {average:.2f}.")