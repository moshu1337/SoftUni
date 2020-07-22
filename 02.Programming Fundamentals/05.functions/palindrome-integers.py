def is_palindrome(text):
    counter = len(text) // 2
    is_palindrome = True

    for i in range(counter):
        second_index = len(text) -1 - i
        if text[i] != text[second_index]:
            is_palindrome = False
            break

    return is_palindrome

def solve(numbers):
    for number in numbers:
        print(is_palindrome(number))

number_list = input().split(", ")
solve(number_list)
