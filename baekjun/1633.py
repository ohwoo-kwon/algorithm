import sys

white = []
black = []
for data in sys.stdin.readlines():
    a, b = data.split()
    white.append(int(a))
    black.append(int(b))

n = len(white)
dp = [[[0] * 16 for _ in range(16)] for _ in range(n + 1)]

for i in range(n):
    for w in range(16):
        for b in range(16):
            if w < 15:
                dp[i + 1][w + 1][b] = max(dp[i + 1][w + 1][b], dp[i][w][b] + white[i])
            if b < 15:
                dp[i + 1][w][b + 1] = max(dp[i + 1][w][b + 1], dp[i][w][b] + black[i])
            dp[i + 1][w][b] = max(dp[i + 1][w][b], dp[i][w][b])

print(dp[n][15][15])