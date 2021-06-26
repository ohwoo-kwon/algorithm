N, K = map(int, input().split()) # N : 물건의 수 / K : 최대 무게

goods = [[0, 0]] + [list(map(int, input().split())) for _ in range(N)]

arr = [[0 for _ in range(K+1)] for _ in range(N+1)]


for r in range(1, N+1):
    for c in range(1, K+1):
        weight = goods[r][0]
        value = goods[r][1]
        if c < weight:
            arr[r][c] = arr[r-1][c] # 현재 물건의 무게보다 작으면 이전 행의 정보를 가져온다
        else:
            arr[r][c] = max(value + arr[r-1][c-weight], arr[r-1][c])

print(arr[N][K])