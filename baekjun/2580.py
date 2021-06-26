def Able(idx):
    global is_finish

    if idx == n:
        is_finish = True
        return
    able = [0] * 10
    r, c = queue[idx]
    Garo(queue[idx][0], queue[idx][1], able)

    for t in range(1, 10):
        if able[t] == 0:
            sdoku[r][c] = t
            Able(idx+1)
            if is_finish:
                return
            else:
                sdoku[r][c] = 0
                continue


def Garo(i, j, able):
    for c in range(9):
        able[sdoku[i][c]] = 1
    for r in range(9):
        able[sdoku[r][j]] = 1
    x = (i // 3) * 3
    y = (j // 3) * 3
    for r in range(x, x+3):
        for c in range(y, y+3):
            able[sdoku[r][c]] = 1
    return able

sdoku = [list(map(int, input().split())) for _ in range(9)]
queue = []
is_finish = False

for i in range(9):
    for j in range(9):
        if sdoku[i][j] != 0:
            continue
        else:
            queue.append([i, j])

n = len(queue)
queue.append([0,0])
Able(0)

for t in range(9):
    print(*sdoku[t])