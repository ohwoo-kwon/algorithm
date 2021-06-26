def Perm(idx):
    if idx == M:
        print(*selected)
        return
    else:
        if idx == 0:
            for i in range(1, N+1):
                selected[idx] = i
                Perm(idx+1)
        else:
            for i in range(selected[idx-1], N+1):
                selected[idx] = i
                Perm(idx+1)




N, M = map(int, input().split())

selected = [0] * M
Perm(0)