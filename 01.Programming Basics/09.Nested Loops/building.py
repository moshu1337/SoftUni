floors = int(input())
rooms = int(input())
type_of_room = ''

for floor in range(1, floors + 1):
    for room in range(0, rooms):
        if floor % 2 == 0:
            type_of_room = "O"
        else:
            type_of_room = "A"
        if floor == floors:
            type_of_room = "L"
    print(f"{type_of_room}{floor}{room}")

# not working prints all on different row
#check building2.py

