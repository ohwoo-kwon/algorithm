def Perm(idx, M, N, result):
    if idx >= M:
        print(*result)
        return

    for i in range(1, N+1):
        if visited[i]: continue
        result.append(i)
        visited[i] = True
        Perm(idx+1, M, N, result)
        visited[i] = False
        result.pop()

N, M = map(int, input().split())
visited = [False] * (N+1)

Perm(0, M, N, [])