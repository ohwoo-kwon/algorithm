from collections import deque

def DFS(V):
    print(V, end=" ")
    visited_dfs[V] = 1
    for i in graph[V]:
        if not visited_dfs[i]:
            DFS(i)

def BFS(V):
    q = deque()
    q.append(V)
    visited_bfs[V] =1
    while q:
        v = q.popleft()
        print(v, end=" ")

        for i in graph[v]:
            if not visited_bfs[i]:
                q.append(i)
                visited_bfs[i] = 1

N, M, V = map(int, input().split())
# 1 <= N(정점의 갯수) <= 1,000 / 1 <= M(간선의 갯수) <10,000 / V(시작 정점)
graph = [[] for _ in range(N+1)] # 정점은 1번 부터 시작하므로 N+1 번 반복

# graph 에 간선 정보를 입력(양방향)
for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

# 각 정점과 연결된 정점들을 오름차순으로 정렬
for i in range(1, N+1):
    graph[i].sort()

# print(graph)

visited_dfs = [0] * (N+1) # DFS에서 이용할 방문 여부
visited_bfs = [0] * (N+1) # BFS에서 이용할 방문 여부

DFS(V)
print()
BFS(V)