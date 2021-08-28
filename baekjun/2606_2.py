def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N = int(input()) # 컴퓨터 수 ( 정점 ) <= 100
M = int(input()) # 컴퓨터 연결 수 ( 간선 )

parent = [i for i in range(N+1)] # 각 정점의 부모

for _ in range(M):
    s, e = map(int, input().split())
    union_parent(parent, s, e)

for i in range(1, N+1):
    find_parent(parent, i)

answer = -1

for i in parent:
    if i == parent[1]:
        answer += 1

print(answer)