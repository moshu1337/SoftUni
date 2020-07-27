cards = input().split()
shuffles = int(input())
middle_of_deck = len(cards) // 2

for _ in range(shuffles):
    result = []

    for index in range(middle_of_deck):
        first_card = cards[index]
        second_card = cards[index + middle_of_deck]

        result.append(first_card)
        result.append(second_card)

    cards = result

print(result)
