from itertools import combinations

def solution(round):
    global ans
    if round == 15:
        ans = 1
        for sub in res:
            if sub.count(0) != 3:
                ans = 0
                break
        return

    t1, t2 = game[round]
    for x,y in ((0,2), (1,1), (2,0)):
        if res[t1][x] > 0 and res[t2][y] > 0:
            res[t1][x] -= 1
            res[t2][y] -= 1
            solution(round + 1)
            res[t1][x] += 1
            res[t2][y] += 1

game = list(combinations(range(6), 2))

for _ in range(4):
    data = list(map(int, input().split()))
    res = [data[i:i+3] for i in range(0, 18, 3)]
    ans = 0
    solution(0)
    print(ans, end=" ")