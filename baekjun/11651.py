import sys

input = sys.stdin.readline

N = int(input())
points = []
for i in range(N):
    y, x = map(int, input().split())
    points.append([x, y])

points.sort()

for i in range(N):
    print(points[i][1], points[i][0])