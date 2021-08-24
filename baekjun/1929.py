M, N = map(int, input().split())

a = [0 for _ in range(N+1)]
a[0] = 1
a[1] = 1
for i in range(2, N+1):
    j = 2
    while i * j <= N:
        a[i*j] = 1
        j += 1

for i in range(M, N+1):
    if a[i] == 0:
        print(i)