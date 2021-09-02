from collections import deque

M, N = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

# 익은 토마토가 있는 위치를 찾은 후 queue 에 넣는다
# queue 에서 하나씩 꺼내어 안 익은 토마토를 익게 만든다

q = deque()

# 익은 토마토들의 위치를 찾아 q 에 담는다
for r in range(N):
    for c in range(M):
        if arr[r][c] == 1:
            q.append((r, c))

dr = [1, -1, 0, 0] # 상 하 좌 우
dc = [0, 0, -1, 1] # 상 하 좌 우

while q:
    now_r, now_c = q.popleft()
    day = arr[now_r][now_c] # 현재 토마토가 익는데 걸린 시간

    for i in range(4):
        next_r = now_r + dr[i]
        next_c = now_c + dc[i]

        # 범위 검사
        if next_r < 0 or next_r >= N or next_c < 0 or next_c >= M:
            continue
        # 토마토가 없으면 되돌아감
        elif arr[next_r][next_c] == -1:
            continue
        # 안 익은 토마토 있을 때
        elif arr[next_r][next_c] == 0:
            arr[next_r][next_c] = day + 1 # 하루 지난 날짜를 넣어주고
            q.append((next_r, next_c))

# 토마토가 모두 익지 못하면 -1 출력, 그 외에는 다 익는데 걸리는 날짜 출력
is_finish = False

for r in range(N):
    for c in range(M):
        # 만약 익지 않은 토마토가 있다면?
        if arr[r][c] == 0:
            is_finish = True # 2중 for 문을 벗어나기 위해 True 로 변경
            break
    if is_finish:
        print(-1)
        break
else: print(day - 1)