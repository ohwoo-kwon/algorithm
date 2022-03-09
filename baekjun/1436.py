N = int(input())
num = 665

while N > 0:
    num += 1
    temp = str(num)
    if "666" in temp:
        N -= 1

print(num)