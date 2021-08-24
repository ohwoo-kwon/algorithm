def Perm(idx):
    if idx == M:
        print(*selected)
        return
    elif idx == 0:
        for i in range(1, N+1):
            if visited[i] == 0:
                visited[i] = 1
                selected[idx] = i
                Perm(idx+1)
                visited[i] = 0
    elif idx != 0:
        for i in range(selected[idx-1]+1, N+1):
            if visited[i] == 0:
                visited[i] = 1
                selected[idx] = i
                Perm(idx+1)
                visited[i] = 0

N, M = map(int, input().split())

visited = [0] * (N+1)
selected = [0] * M

Perm(0)