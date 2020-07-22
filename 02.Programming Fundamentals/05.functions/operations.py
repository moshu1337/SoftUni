def operation_with_numbers(a, b, operation):
    if operation == 'add':
        return a + b
    if operation == 'subtract':
        return a - b
    if operation == 'divide':
        return a // b  # you can also cast it to integer
    if operation == 'multiply':
        return a * b


operation_to_be_done = input()
first_number = int(input())
second_number = int(input())


print(operation_with_numbers(first_number, second_number, operation_to_be_done))
