import math

speed = float(input())
liters = float(input())
to_moon_and_back = 384400 * 2
time_sum = to_moon_and_back / speed
total_time = time_sum + 3
gorivo_needed = ( liters * to_moon_and_back) / 100

print(math.ceil(total_time))
print(math.ceil(gorivo_needed))
