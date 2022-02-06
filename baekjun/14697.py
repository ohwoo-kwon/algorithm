a, b, c, n = map(int, input().split())
dp = [0] * 301
dp[a] = dp[b] = dp[c] = 1

for i in range(a, n+1):
    for j in [a, b, c]:
        if dp[i] == 1 and i+j < n+1:
            dp[i+j] = 1

print(dp[n])