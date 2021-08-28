def DFS(x, y):
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    stack = [(x, y)]
    arr[x][y] = '0' # 현재 위치를 0으로 바꿔줌
    cnt = 1 # 현재 단지의 아프트 갯수는 1

    while stack:
        r, c = stack.pop()

        for i in range(4):
            nr = r + dr[i] # 연결된 위치로 이동
            nc = c + dc[i] # 연결된 위치로 이동
            if nr < 0 or nr >= N or nc < 0 or nc >= N: # 범위를 벗어나면 생략하고 위로 돌아감
                continue
            if arr[nr][nc] == '1': # 연결된 아파트가 있으면
                arr[nr][nc] = '0' # 0 으로 바꾸고
                cnt += 1 # 아프트 갯수 1개 더해주고
                stack.append((nr, nc)) # 스택에 넣어준다

    result.append(cnt)

N = int(input())
arr = [list(input()) for _ in range(N)]

dangi = 0 # 단지의 갯수
result = [] # 각 단지의 아파트 수

for r in range(N):
    for c in range(N):
        if arr[r][c] == '1': # 집이 존재하면 DFS 함수를 통해 연결된 집들 0으로 바꿈
            DFS(r, c)
            dangi += 1 # 단지 수를 1개 증가

print(dangi)
result.sort() # 오름차순으로 정렬
for num in result:
    print(num)