for i in range(4):
    points = list(map(int, input().split()))

    if points[2] < points[4] or points[3] < points[5] or points[0] > points[6] or points[1] > points[7]:
        print("d")
    elif points[2] == points[4] and points[3] == points[5]:
        print("c")
    elif points[2] == points[4] and points[1] == points[7]:
        print("c")
    elif points[0] == points[6] and points[3] == points[5]:
        print("c")
    elif points[0] == points[6] and points[1] == points[7]:
        print("c")
    elif points[2] == points[4] and not (points[3] < points[5]) and not (points[1] > points[7]):
        print("b")
    elif points[0] == points[6] and not (points[3] < points[5]) and not (points[1] > points[7]):
        print("b")
    elif points[1] == points[7] and not (points[0] > points[6]) and not (points[2] < points[4]):
        print("b")
    elif points[3] == points[5] and not (points[0] > points[6]) and not (points[2] < points[4]):
        print("b")
    else:
        print("a")