INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
distance = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def get_smallest_node():
    idx = 0
    minV = INF
    for i in range(1, n+1):
        if distance[i] < minV and not visited[i]:
            idx = i
            minV = distance[i]
    return idx

def dijkstra(start):
    distance[start] = 0
    visited[start] = 1
    for j in graph[start]:
        distance[j[0]] = j[1]
    for _ in range(n-1):
        now = get_smallest_node()
        visited[now] = 1
        for j in graph[now]:
            cost = distance[now] + j[1]
            distance[j[0]] = min(cost, distance[j[0]])

dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])
