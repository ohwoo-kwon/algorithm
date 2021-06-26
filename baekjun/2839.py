N = int(input())

five = N // 5

if five == 0:
    if N % 3 == 0:
        print(N // 3)
    else:
        print(-1)
else:
    for i in range(five, -1, -1):
        remain = N - 5 * i
        if remain % 3 == 0:
            print(i + remain // 3)
            break
        else:
            continue
    else: print(-1)