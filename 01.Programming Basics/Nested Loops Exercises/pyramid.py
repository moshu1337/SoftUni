n = int(input())
number = 1
clos = 1
while number <= n:
    for i in range(clos):
        if number > n:
            break
        print(number, end=" ")
        number += 1
    print()
    clos +=1

