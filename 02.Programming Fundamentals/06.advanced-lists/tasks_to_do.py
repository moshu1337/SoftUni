tasks = []

while True:
    command = input()
    if command == 'End':
        break
    tokens = command.split('-')
    priority = tokens[0]
    task = tokens[1]
    tasks.append((priority,task))

tasks_in_priority = [task_name for priority, task_name in sorted(tasks)]
print(tasks_in_priority)