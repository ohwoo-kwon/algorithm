hour, minute = input().split()
hour = int(hour)
minute = int(minute)

hour += 24
minute = minute + hour * 60
minute -= 30
hour = minute / 60
hour = hour % 24
minute = minute % 60

print(int(hour), int(minute))