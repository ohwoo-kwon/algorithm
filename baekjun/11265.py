N, M = map(int, input().split())
roads = []
for _ in range(N):
    roads.append(list(map(int, input().split())))

for k in range(N):
    for i in range(N):
        for j in range(N):
            if roads[i][j] > roads[i][k] + roads[k][j]:
                roads[i][j] = roads[i][k] + roads[k][j]

for _ in range(M):
    A, B, C = map(int, input().split())
    A -= 1
    B -= 1
    if roads[A][B] <= C:
        print("Enjoy other party")
    else: print("Stay here")
