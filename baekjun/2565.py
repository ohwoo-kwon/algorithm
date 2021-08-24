N = int(input())

lines = [list(map(int, input().split())) for _ in range(N)]

lines = sorted(lines, key=lambda line:line[1])
i = 0
sm = [0] * N

for i in range(N):
    cnt = 0
    for j in range(i):
        if lines[i][0] > lines[j][0] and sm[i] < sm[j]:
            sm[i] = sm[j]
    sm[i] += 1

print(N-max(sm))