from collections import defaultdict
n = int(input())
student_grades = defaultdict(list)

for _ in range(n):
    name = input()
    grade = float(input())
    student_grades[name].append(grade)

students_average_grade = defaultdict(float)

for student, grades in student_grades.items():
    average_grade = sum(grades) / len(grades)
    if average_grade >= 4.50:
        students_average_grade[student] += average_grade

for student, grade in sorted(students_average_grade.items(), key=lambda x: -x[1]):
    print(f"{student} -> {grade:.2f}")

