N = int(input()) # 컴퓨터 수 ( 정점 ) <= 100
M = int(input()) # 컴퓨터 연결 수 ( 간선 )

graph = [[] for _ in range(N+1)] # 각 컴퓨터의 연결 정보를 담을 그래프
visited = [0 for _ in range(N+1)] # 방문 여부

for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s) # 양방향

result = 0 # 바이러스에 감염된 컴퓨터 수

stack = [1] # DFS를 이용하여 풀 경우 stack 이용
visited[1] = 1 # 1번 노드 방문 처리

while stack: # stack 이 빌 때까지 반복
    now = stack.pop() # 스택에서 마지막 정점을 꺼낸다
    result += 1 # 감염된 컴퓨터 수 1 증가

    for i in graph[now]: # 현재 정점과 연결된 정점들 찾아서
        if not visited[i]: # 방문하지 않았으면
            stack.append(i) # 스택에 넣어준다
            visited[i] = 1 # 해당 노드 방문 처리

print(result-1) # 1번 컴퓨터를 제외하므로 -1