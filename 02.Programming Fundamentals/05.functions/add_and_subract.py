def add(a, b):
    return a + b


def subtract(a, b):
    return a - b

def solve(a, b, c):
    addition = add(a ,b)
    res = subtract(addition, c)
    return res




a = int(input())
b = int(input())
c = int(input())

print(solve(a, b, c))
