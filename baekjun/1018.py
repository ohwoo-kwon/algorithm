import copy

N, M = map(int, input().split())

chess = [[0 for _ in range(M+2)]] + [[0] + list(input()) + [0] for _ in range(N)] + [[0 for _ in range(M+2)]]
check = []

for i in range(1, N-6): # 행 반복
    for j in range(1, M-6): # 열 반복
        idx1 = 0
        idx2 = 0
        for r in range(8):
            for k in range(8):
                if (i+r+j+k) % 2 == 0:
                    if chess[i+r][j+k] != "W": idx1 += 1
                    if chess[i+r][j+k] != "B": idx2 += 1
                else:
                    if chess[i+r][j+k] != "B": idx1 += 1
                    if chess[i+r][j+k] != "W": idx2 += 1
        check += [idx1]
        check += [idx2]

print(f"{min(check)}")