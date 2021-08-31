from collections import deque

N, M = map(int, input().split())

arr = [list(input()) for _ in range(N)] # 미로 정보를 2차원 배열로 받는다 (String 으로 받음)

# 시작점의 이동거리를 1로 두고, BFS 방식을 이용하여 1칸 씩 이동할 때 마다 거리를 1 씩 증가시켜서 arr 에 저장한다
# N, M 위치에 거리를 저장하면 그 이동거리를 출력

q = deque() # queue 를 만든다
q.append([0, 0])
arr[0][0] = 1 # 시작점의 이동 거리를 1 로 수정

while q: # q 에 값이 있는 동안 반복
    r, c = q.popleft() # queue 에서 가장 앞에 있는 값 가져오기
    dis = arr[r][c]

    dr = [-1, 1, 0, 0] # 상 하 좌 우
    dc = [0, 0, -1, 1] # 상 하 좌 우

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if nr < 0 or nr >= N or nc < 0 or nc >=M: # 범위를 벗어나는지 체크
            continue
        elif arr[nr][nc] == '1': # 이동할 수 있는 길이라면
            arr[nr][nc] = dis + 1 # 이전 이동 거리에서 1 을 더해서 넣어준다
            q.append([nr, nc]) # queue 에 넣어준다

print(arr[N-1][M-1])