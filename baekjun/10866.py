N = int(input())

queue = [0] * N
f = -1
r = -1
for _ in range(N):
    info = list(input().split())

    if info[0] == 'push_front':
        for i in range(r+1, f+1, -1):
            queue[i] = queue[i-1]
        queue[f+1] = info[1]
        r += 1
    elif info[0] == 'push_back':
        r += 1
        queue[r] = info[1]
    elif info[0] == 'pop_front':
        if f == r:
            print(-1)
        else:
            f += 1
            print(queue[f])
    elif info[0] == 'pop_back':
        if f == r:
            print(-1)
        else:
            print(queue[r])
            r -= 1
    elif info[0] == 'size':
        print(r - f)
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
    else:
        if f == r:
            print(-1)
        else:
            print(queue[r])