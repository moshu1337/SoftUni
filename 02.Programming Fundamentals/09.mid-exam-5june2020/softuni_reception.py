employee_efficiency_1 = int(input())
employee_efficiency_2 = int(input())
employee_efficiency_3 = int(input())
students_count = int(input())
time_needed = 0
hour = 0
students_answered_per_hour = employee_efficiency_1 + employee_efficiency_2 + employee_efficiency_3

while students_count > 0:
    hour += 1
    if hour % 4 == 0:
        time_needed += 1
        continue
    time_needed += 1
    students_count -= students_answered_per_hour

print(f"Time needed: {time_needed}h.")


