def solution(priorities, location):
    answer = 1
    q = []
    for idx in range(len(priorities)):
        q.append([priorities[idx], idx])

    while q:
        priority, idx = q.pop(0)
        max_priority = priority
        cnt = 0
        flag = False
        for i in range(len(q)):
            if max_priority < q[i][0]:
                max_priority = q[i][0]
                cnt = i
                flag = True
                continue
        if flag:
            q.append([priority, idx])
        else:
            if idx == location:
                return answer
            else:
                answer += 1
        while cnt > 0:
            q.append(q.pop(0))
            cnt -= 1
    return answer


print(solution([2, 1, 3, 2], 2))