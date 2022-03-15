S = int(input())

i = 1

while True:
    result = i * (i+1) // 2
    if result > S:
        print(i-1)
        break
    i += 1