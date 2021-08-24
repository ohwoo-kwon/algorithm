def Star(N):
    if N == 3:
        map[0][:3] = map[2][:3] = [1, 1, 1]
        map[1] = [1, 0, 1]
    else:
        n = N // 3
        Star(n)
        for i in range(3):
            for j in range(3):
                if i == 1 and j == 1:
                    continue
                for k in range(n):
                    map[n*i+k][n*j:n*(j+1)] = map[k][:n]



N = int(input())
map = [[0 for _ in range(N)] for _ in range(N)]
Star(N)
for i in range(N):
    for j in range(N):
        if map[i][j]:
            print("*", end="")
        else:
            print(" ", end="")
    print()