import math


def solution(progresses, speeds):
    answer = []
    remain = []
    for i in range(len(progresses)):
        remain_day = math.ceil((100 - progresses[i]) / speeds[i])
        remain.append(remain_day)
    i = 1;
    cnt = 1
    cur = remain[0]
    while i < len(remain):
        if cur < remain[i]:
            answer.append(cnt)
            cnt = 1
            cur = remain[i]
        else:
            cnt += 1
        i += 1
    answer.append(cnt)

    return answer

print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))