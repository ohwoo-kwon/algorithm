import sys

input = sys.stdin.readline
f = r = -1
queue = [0] * 2000001
N = int(input())
for _ in range(N):
    info = list(input().split())
    if info[0] == 'push':
        r += 1
        queue[r] = info[1]
    elif info[0] == 'pop':
        if f == r:
            print(-1)
        else:
            f += 1
            print(queue[f])
    elif info[0] == 'size':
        print(r-f)
    elif info[0] == 'empty':
        if f == r:
            print(1)
        else:
            print(0)
    elif info[0] == 'front':
        if f == r:
            print(-1)
        else:
            print(queue[f+1])
    elif info[0] == 'back':
        if f == r:
            print(-1)
        else:
            print(queue[r])