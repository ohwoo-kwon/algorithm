for t in range(1, int(input())+1):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    diff = ((x1-x2)**2 + (y1-y2)**2) ** 0.5
    r = r1 + r2
    R = abs(r1-r2)

    if diff > r:
        print(0)
    elif diff < R:
        print(0)
    elif diff == 0 and R == 0:
        print(-1)
    elif diff == r or diff == R:
        print(1)
    else:
        print(2)