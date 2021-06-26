N, M = map(int, input().split())

maps = [[0]*(N+1)] + [[0] + list(map(int, input().split())) for _ in range(N)]

positions_c = [0]
positions_h = [0]
chickens = 0
houses = 0
for r in range(1, N+1):
    for c in range(1, N+1):
        if maps[r][c] == 2:
            chickens += 1
            positions_c.append((r, c))
        elif maps[r][c] == 1:
            houses += 1
            positions_h.append((r,c))

distances = [[0 for _ in range(chickens+1)] for _ in range(houses+1)]
selected = [0] * (chickens+1)

for r in range(1, houses+1):
    min_value = [100, 0]
    for c in range(1, chickens+1):
        distances[r][c] = abs(positions_c[c][0] - positions_h[r][0]) + abs(positions_c[c][1] - positions_h[r][1])
        if min_value[0] > distances[r][c]:
            min_value[0] = distances[r][c]
            min_value[1] = c
    selected[min_value[1]] += 1

rm = chickens - M
while rm > 0:
    min_value = 100
    for i in range(1, chickens+1):
        if selected[i] < min_value:
            min_value = selected[i]
            idx = i
    selected[idx] = 100
    for r in range(1, houses+1):
        distances[r][idx] = 100
    rm -= 1
result = 0
for r in range(1, houses+1):
    min_value = 100
    for c in range(1, chickens+1):
        if min_value > distances[r][c]:
            min_value = distances[r][c]
    result += min_value

print(result)
