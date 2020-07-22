from collections import defaultdict
command = input()
company_users = defaultdict(list)
while command != 'End':
    args = command.split(" -> ")
    company = args[0]
    id = args[1]
    if id in company_users[company]:
        continue
    company_users[company].append(id)
    command = input()

sorted_employees = dict(sorted(company_users.items(), key=lambda c: c[0]))

for key, value in sorted_employees.items():
    print(f"{key}")
    for employees_id in value:
        print(f"-- {employees_id}")