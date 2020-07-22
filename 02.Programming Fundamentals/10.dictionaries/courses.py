from collections import defaultdict
courses = defaultdict(list)
command = input()
while command != 'end':
    args = command.split(" : ")
    course = args[0]
    student = args[1]
    courses[course].append(student)
    command = input()
sorted_courses = dict(sorted(courses.items(), key=lambda c: len(c[1]), reverse=True))

for key, value in sorted_courses.items():
    print(f"{key}: {len(value)}")
    for student in sorted(value):
        print(f"-- {student}")
