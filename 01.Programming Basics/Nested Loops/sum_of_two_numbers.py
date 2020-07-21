start_num = int(input())
end_number = int(input())
magic_number = int(input())
count = 0
is_found = False
for n1 in range(start_num, end_number + 1):
    for n2 in range(start_num, end_number + 1):
        count += 1
        if n1 + n2 == magic_number:
            is_found = True
            print(f"Combination N:{count} ({n1} + {n2} = {magic_number})")
            break
    if is_found:
        break
if not is_found:
    print(f"{count} combinations - neither equals {magic_number}")
