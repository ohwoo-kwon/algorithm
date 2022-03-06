def go(idx, total):
    if total < 0:
        return -9000000

    if idx == N:
        return 0

    if dp[idx][total] != -1:
        return dp[idx][total]

    walk = go(idx+1, total - arr[idx][0])
    walk_money = walk + arr[idx][1]
    bike = go(idx+1, total - arr[idx][2])
    bike_money = bike + arr[idx][3]
    dp[idx][total] = max(walk_money, bike_money)
    return dp[idx][total]


N, K = map(int, input().split())
dp = [[-1] * (K+1) for _ in range(N)]
arr = [list(map(int, input().split())) for _ in range(N)]
print(go(0, K))