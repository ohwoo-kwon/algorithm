import sys
input = sys.stdin.readline

N, M = map(int, input().split())

parent = [[] for _ in range(N+1)]

for _ in range(M):
    p, c = map(int, input().split())
    parent[c].append(p)

stack = [int(input())]
result = 0
visited = [False] * (N+1)
while stack:
    v = stack.pop()
    for p in parent[v]:
        if not visited[p]:
            visited[p] = True
            stack.append(p)
            result += 1
print(result)
