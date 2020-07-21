lenght = int(input())
width = int(input())
height = int(input())
precent_volume_taken = float(input())

total_volume = lenght * width * height
total_volume = total_volume / 1000
precent = precent_volume_taken * 0.01
volume_taken = total_volume / 100
volume_left = total_volume - volume_taken
print(f'{volume_left:.2f}')
