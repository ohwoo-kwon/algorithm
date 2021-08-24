hour, minute = input().split()

hour = int(hour)
minute = int(minute)

if hour != 0:
    if minute >= 30:
        print(hour, minute - 30)
    else:
        print(hour -1, minute + 30)
else:
    if minute >= 30:
        print(hour, minute - 30)
    else:
        print(23, minute + 30)