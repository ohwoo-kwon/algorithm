import sys

input = sys.stdin.readline
N, Q = map(int, input().split())
owned = [False] * (N+1)
for _ in range(Q):
    cur = int(input())
    temp = cur
    flag = False

    while temp != 1:
        # 소유 했다면
        if owned[temp]:
            flag = True
            first_owned = temp
        temp //= 2
    if flag:
        print(first_owned)
    else:
        owned[cur] = True
        print(0)