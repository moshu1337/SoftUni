width = int(input())
lenght = int(input())
total_pieces_started = width * lenght
used_pieces = 0
total_pieces = total_pieces_started

while True:
    command = input()
    if command == "STOP":
        print(f"{total_pieces_started - used_pieces} pieces are left.")
        break
    total_pieces -= int(command)
    used_pieces += int(command)
    if used_pieces > total_pieces_started:
        print(f"No more cake left! You need {used_pieces - total_pieces_started} pieces more.")
        break
