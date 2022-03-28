bingo_board = {}
width = [0] * 5
height = [0] * 5
diagonal = [0] * 2
bingo = 0
answer = 0

for i in range(5):
    temp = input().split()
    for j in range(5):
        bingo_board[temp[j]] = (i, j)

for _ in range(5):
    if bingo >= 3:
        break
    nums = input().split()
    for num in nums:
        answer += 1
        r, c = bingo_board[num]
        width[r] += 1
        if width[r] == 5: bingo += 1
        height[c] += 1
        if height[c] == 5: bingo += 1
        if r == c:
            diagonal[0] += 1
            if diagonal[0] == 5:
                bingo += 1
        if r + c == 4:
            diagonal[1] += 1
            if diagonal[1] == 5:
                bingo += 1
        if bingo >= 3:
            print(answer)
            break

