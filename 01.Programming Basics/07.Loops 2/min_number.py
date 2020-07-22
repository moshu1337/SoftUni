n = int(input())
minavane = 0
smallest_num = 0
while minavane < n:
    curr_num = int(input())
    if minavane == 0:
        smallest_num = curr_num
    elif curr_num < smallest_num:
        smallest_num = curr_num
    minavane += 1

print(smallest_num)