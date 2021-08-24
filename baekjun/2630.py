def Merge(rs, rm, re, cs, cm, ce):
    global white, blue
    if rs == re or cs == ce:
        if squares[rs][cs] == 0:
            white += 1
        else:
            blue += 1
        return

    temp = squares[rs][cs]
    for r in range(rs, re+1):
        for c in range(cs, ce+1):
            if temp != squares[r][c]:
                Merge(rs, (rs+rm)//2, rm, cs, (cs+cm)//2, cm)
                Merge(rs, (rs+rm)//2, rm, cm+1, (cm+ce+1)//2, ce)
                Merge(rm+1, (re+rm+1)//2, re, cs, (cs+cm)//2, cm)
                Merge(rm+1, (re+rm+1)//2, re, cm+1, (cm+ce+1)//2, ce)
                return
    if temp == 0:
        white += 1
    else: blue += 1


N = int(input())
squares = [list(map(int, input().split())) for _ in range(N)]
white = 0
blue = 0

Merge(0, (N-1)//2, N-1, 0, (N-1)//2, N-1)

print(white)
print(blue)