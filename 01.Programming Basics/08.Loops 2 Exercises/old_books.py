searched_book = input()
capacity = int(input())
counter = 0

while counter < capacity:
    book = input()
    if searched_book == book:
        print(f"You checked {counter} books and found it.")
        break
    counter += 1

if counter == capacity:
    print("The book you search is not here!")
    print(f"You checked {counter} books.")
