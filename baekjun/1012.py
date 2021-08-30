def DFS(y, x):
    stack = [(y, x)] # stack 에 주어진 위치를 담는다
    arr[y][x] = 0 # 해당 위치를 0으로 바꿈

    dr = [1, 0, -1, 0] # 하 우 상 좌
    dc = [0, 1, 0, -1] # 하 우 상 좌

    while stack:
        r, c = stack.pop()

        for i in range(4): # 상하좌우 탐색을 위해 4번 반복
            nr = r + dr[i]
            nc = c + dc[i]

            if nr < 0 or nr >= N or nc < 0 or nc >= M: # nr 혹은 nc 가 범위를 벗어나면 되돌아간다
                continue
            elif arr[nr][nc] == 1: # 해당 위치에 배추가 있다면
                stack.append((nr, nc)) # stack 에 추가
                arr[nr][nc] = 0 # 해당 위치 0으로 수정

tc = int(input())

for _ in range(tc):
    M, N, K = map(int, input().split()) # M : 가로 / N : 세로 / K : 배추 수

    arr = [[0] * M for _ in range(N)] # N X M 행렬 생성

    for _ in range(K): # 배추가 심어져 있는 위치는 1로 수정
        x, y = map(int, input().split())
        arr[y][x] = 1

    result = 0 # 필요한 지렁이 수

    for r in range(N):
        for c in range(M):
            if arr[r][c] == 1:
                DFS(r, c)
                result += 1

    print(result)