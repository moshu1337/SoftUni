n = int(input())

counter = 0
biggest_number = 0
while counter < n:
    curr_num = int(input())
    if counter == 0:
        biggest_number = curr_num
    elif curr_num > biggest_number:
        biggest_number = curr_num
    counter += 1

print(biggest_number)
