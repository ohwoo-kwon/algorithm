N = int(input())

points = []
for i in range(N):
    a, b = map(int, input().split())
    points.append([a, b])

points = sorted(points)
for i in range(N):
    print(points[i][0], points[i][1])