N, K = map(int, input().split())

queue = [i for i in range(1,N+1)] + [0] * 1000000

f = 0
r = N - 1
print('<', end='')
while r != f:
    for _ in range(K-1):
        r += 1
        queue[r] = queue[f]
        f += 1
    print(queue[f], end=', ')
    f += 1
print('{}>' .format(queue[f]))