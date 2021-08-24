N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# -1, 0, 1 종이의 갯수
cnt_1 = 0
cnt0 = 0
cnt1 = 0

# 종이가 일정한지 확인하는 함수
def check_paper(r, c, k): # r : 시작 행 / c : 시작 열 / k : 종이의 크기
    global cnt_1, cnt0, cnt1
    v = arr[r][c] # 비교 대상이 되는 숫자
    for i in range(k):
        for j in range(k):
            if arr[r+i][c+j] != v:
                return False
    if v == -1:
        cnt_1 += 1
    elif v == 0:
        cnt0 += 1
    elif v == 1:
        cnt1 += 1

    return True

# 종이를 9등분 하는 함수
def divide_nine(r, c, k):
    new_k = k // 3
    if not check_paper(r, c, new_k):
        divide_nine(r, c, new_k)

    if not check_paper(r, c+new_k, new_k):
        divide_nine(r, c+new_k, new_k)

    if not check_paper(r, c+2*new_k, new_k):
        divide_nine(r, c+2*new_k, new_k)

    if not check_paper(r+new_k, c, new_k):
        divide_nine(r+new_k, c, new_k)

    if not check_paper(r+new_k, c+new_k, new_k):
        divide_nine(r+new_k, c+new_k, new_k)

    if not check_paper(r+new_k, c+2*new_k, new_k):
        divide_nine(r+new_k, c+2*new_k, new_k)

    if not check_paper(r+2*new_k, c, new_k):
        divide_nine(r+2*new_k, c, new_k)

    if not check_paper(r+2*new_k, c+new_k, new_k):
        divide_nine(r+2*new_k, c+new_k, new_k)

    if not check_paper(r+2*new_k, c+2*new_k, new_k):
        divide_nine(r+2*new_k, c+2*new_k, new_k)


if not check_paper(0, 0, N):
    divide_nine(0, 0, N)
print(cnt_1)
print(cnt0)
print(cnt1)
