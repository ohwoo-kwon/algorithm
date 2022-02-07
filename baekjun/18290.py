import sys
input = sys.stdin.readline


def perm(i, cnt, x, y):
    if i == K:
        global result
        result = max(result, cnt)
        return

    for r in range(x, N):
        for c in range(y if x == r else 0, M):
            if visited[r][c]:
                continue
            for j in range(4):
                nr = r + dr[j]
                nc = c + dc[j]
                if 0 <= nr < N and 0 <= nc < M and visited[nr][nc]:
                    break
            else:
                visited[r][c] = True
                perm(i+1, cnt + arr[r][c], r, c)
                visited[r][c] = False


N, M, K = map(int, input().split())
arr = []
result = -40001
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
for _ in range(N):
    temp = list(map(int, input().split()))
    arr.append(temp)

visited = [[False for _ in range(M)] for _ in range(N)]
perm(0, 0, 0, 0)
print(result)