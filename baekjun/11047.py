N, K = map(int, input().split())

coins = [int(input()) for _ in range(N)]


cnt = 0

for i in range(N-1, -1, -1):
    coin = coins[i]
    cnt += (K // coin)
    K %= coin
    if coin == 0:
        break

print(cnt)