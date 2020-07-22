number_of_rooms = int(input())
free_chairs = 0
enough_chairs = True
for room in range(1, number_of_rooms + 1):
    room_data = input().split()
    chair_count = len(room_data[0])
    taken_places = int(room_data[1])
    if chair_count > taken_places:
        free_chairs += chair_count - taken_places
    elif taken_places > chair_count:
        needed_chairs_in_room = taken_places - chair_count
        print(f'{needed_chairs_in_room} more chairs needed in room {room}')
        enough_chairs = False

if enough_chairs:
    print(f'Game On, {free_chairs} free chairs left')
