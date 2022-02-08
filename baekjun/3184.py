R, C = map(int, input().split())

# 마당 정보를 받는다
# 마당과 같은 크기의 행열에 방문 여부 체크
# 0,0 을 시작으로 같은 영역 안에 있는 양과 늑대의 수를 체크한다 DFS 사용
# 체크한 영역은 방문 여부 체크하는 행열에 체크한다
# 한 영역을 다 체크하면 늑대와 양의 수를 비교하여 최종 남는 늑대와 양의 수를 계산

visited = [[False for _ in range(C)] for _ in range(R)]
ground = []
for _ in range(R):
    ground.append(list(input()))
result = [0, 0]
stack = []
for r in range(R):
    for c in range(C):
        if not visited[r][c] and ground[r][c] != "#":
            stack.append((r, c))
            visited[r][c] = True
            sheep = 0
            wolf = 0
            while stack:
                sr, sc = stack.pop()
                dr = [1, -1, 0, 0]
                dc = [0, 0, 1, -1]
                if ground[sr][sc] == "o":
                    sheep += 1
                elif ground[sr][sc] == "v":
                    wolf += 1

                for i in range(4):
                    nr = sr + dr[i]
                    nc = sc + dc[i]
                    if nr < 0 or nr >= R or nc < 0 or nc >= C or visited[nr][nc] or ground[nr][nc] == "#":
                        continue
                    stack.append((nr, nc))
                    visited[nr][nc] = True
            if sheep > wolf:
                result[0] += sheep
            else:
                result[1] += wolf

print(*result)