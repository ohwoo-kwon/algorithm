width, height = map(int,input().split())
stores = int(input())
locations = []
for _ in range(stores):
    locations += [list(map(int, input().split()))]

my_location = list(map(int, input().split()))
distance = 0

for location in locations:
    if my_location[0] == 1:
        if location[0] == 1:
            distance += abs(location[1] - my_location[1])
        elif location[0] == 2:
            value = location[1] + my_location[1]
            if value < width:
                distance += value + height
            else:
                distance += width + width - value + height
        elif location[0] == 3:
            distance += location[1] + my_location[1]
        else:
            distance += location[1] + width - my_location[1]
    elif my_location[0] == 2:
        if location[0] == 2:
            distance += abs(location[1] - my_location[1])
        elif location[0] == 1:
            value = location[1] + my_location[1]
            if value < width:
                distance += value + height
            else:
                distance += width + width - value + height
        elif location[0] == 3:
            distance += height - location[1] + my_location[1]
        else:
            distance += height - location[1] + width - my_location[1]
    elif my_location[0] == 3:
        if location[0] == 1:
            distance += my_location[1] + location[1]
        elif location[0] == 2:
            distance += height - my_location[1] + location[1]
        elif location[0] == 3:
            distance += abs(location[1] - my_location[1])
        else:
            value = location[1] + my_location[1]
            if value < height:
                distance += width + value
            else:
                distance += width + height + height - value
    else:
        if location[0] == 1:
            distance += my_location[1] + width - location[1]
        elif location[0] == 2:
            distance += height - my_location[1] + width - location[1]
        elif location[0] == 4:
            distance += abs(location[1] - my_location[1])
        else:
            value = location[1] + my_location[1]
            if value < height:
                distance += width + value
            else:
                distance += width + height + height - value
print(distance)