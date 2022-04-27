dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


def is_ok(r, c):
    if r < 0 or r >= 5 or c < 0 or c >= 5:
        return False
    return True


def find_PP(place, r, c):
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if is_ok(nr, nc) and place[nr][nc] == 'P':
            return True
    return False


def find_POP(place, r, c):
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if not is_ok(nr, nc):
            continue
        if place[nr][nc] == 'O':
            for j in range(4):
                snr = nr + dr[j]
                snc = nc + dc[j]
                if is_ok(snr, snc) and (snr != r or snc != c) and place[snr][snc] == 'P':
                    return True
    return False


def bfs(place):
    for r in range(5):
        for c in range(5):
            if place[r][c] == 'P':
                if find_PP(place, r, c): return 0
                if find_POP(place, r, c): return 0
    return 1


def solution(places):
    answer = []
    global temp
    for place in places:
        result = bfs(place)
        answer.append(result)
    return answer
