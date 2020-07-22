employee_happiness = [int(n) for n in input().split()]
factor = int(input())
multiplied_happiness = [v * factor for v in employee_happiness]
average_happiness = sum(multiplied_happiness) / len(multiplied_happiness)
happy_values = list(filter(lambda n: n >= average_happiness, multiplied_happiness))
happy_count = len(happy_values)
total_count = len(employee_happiness)

if len(happy_values) >= (len(employee_happiness) / 2):
    print(f'Score: {happy_count}/{total_count}. Employees are happy!')
else:
    print(f'Score: {happy_count/total_count}, Employees are not happy!')
     