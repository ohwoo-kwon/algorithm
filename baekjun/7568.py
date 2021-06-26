N = int(input())

peoples = []

for _ in range(N):
    peoples += [list(map(int, input().split()))]

rank = []

for i in range(N):
    cnt = 0
    for j in range(N):
        if peoples[i][0] < peoples[j][0] and peoples[i][1] < peoples[j][1]:
            cnt += 1
    rank += [cnt + 1]
print(*rank)