def solution(board, skill):
    answer = 0
    temp_array = [[0 for _ in range(len(board[0]) + 1)] for _ in range(len(board) + 1)]

    for skill_type, r1, c1, r2, c2, degree in skill:
        if skill_type == 1:
            degree = -degree
        temp_array[r1][c1] += degree
        temp_array[r1][c2 + 1] -= degree
        temp_array[r2 + 1][c1] -= degree
        temp_array[r2 + 1][c2 + 1] += degree

    for r in range(len(temp_array)):
        for c in range(1, len(temp_array[0])):
            temp_array[r][c] += temp_array[r][c - 1]

    for c in range(len(temp_array[0]) - 1):
        for r in range(1, len(temp_array)):
            temp_array[r][c] += temp_array[r - 1][c]

    for r in range(len(board)):
        for c in range(len(board[0])):
            board[r][c] += temp_array[r][c]
            if board[r][c] > 0: answer += 1
    return answer