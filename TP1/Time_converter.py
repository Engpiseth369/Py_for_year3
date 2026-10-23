total_seconds = 9875

# a
hours = total_seconds // 3600
remainder = total_seconds % 3600
minutes = remainder // 60
seconds = remainder % 60

print(f"{total_seconds} seconds = {hours} h {minutes} min {seconds} s")

# b
rebuild = hours*3600 + minutes*60 + seconds
print("Check:", total_seconds == rebuild)

# c
test_1 = 3600

hours_1 = test_1 // 3600
remainder_1 = test_1 % 3600
minutes_1 = remainder_1 // 60
seconds_1 = remainder_1 % 60

print(f"{test_1} seconds = {hours_1} h {minutes_1} min {seconds_1} s")

rebuild_1 = hours_1*3600 + minutes_1*60 + seconds_1
print("Check:", test_1 == rebuild_1)

test_2 = 59

hours_2 = test_2 // 3600
remainder_2 = test_2 % 3600
minutes_2 = remainder_2 // 60
seconds_2 = remainder_2 % 60

print(f"{test_2} seconds = {hours_2} h {minutes_2} min {seconds_2} s")

rebuild_2 = hours_2*3600 + minutes_2*60 + seconds_2
print("Check:", test_2 == rebuild_2)

test_3 = 86399

hours_3 = test_3 // 3600
remainder_3 = test_3 % 3600
minutes_3 = (test_3 % 3600) // 60
seconds_3 = test_3 % 60

print(f"{hours_3} seconds = {hours_3} h {minutes_3} min {seconds_3} s")

rebuild_3 = hours_3*3600 + minutes_3*60 + seconds_3
print("Check:", test_3 == rebuild_3)
