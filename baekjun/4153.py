while True:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break

    if a > b and a > c:
        if a < b + c and a**2 == b**2 + c**2:
            print("right")
        else:
            print("wrong")
    elif b > c and b > a:
        if b < a + c and b**2 == a**2 + c**2:
            print("right")
        else:
            print("wrong")
    elif c > b and c > a:
        if c < a + b and c**2 == a**2 + b**2:
            print("right")
        else:
            print("wrong")