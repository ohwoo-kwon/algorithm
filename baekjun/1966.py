from collections import deque

for _ in range(int(input())):
    N, M = map(int, input().split())
    q = deque(list(map(int, input().split())))
    idx = deque([i for i in range(N)])
    result = 0
    while True:
        maxV = max(q)
        while True:
            n = q.popleft()
            i = idx.popleft()
            if n == maxV:
                result += 1
                break
            else:
                q.append(n)
                idx.append(i)
        if i == M:
            print(result)
            break