import sys
numbers = input().split()
remove = int(input())
for _ in range(remove):
    small = []
    minimum = sys.maxsize
    for n in numbers:
        num = int(n)
        small.append(num)
        if num <= minimum:
            minimum = num
    small.remove(minimum)
    numbers = small
print(numbers)
