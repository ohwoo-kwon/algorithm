N, M = map(int, input().split())
cards = list(map(int, input().split()))

max_result = 0

for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            result = cards[i] + cards[j] + cards[k]
            if result > M:
                continue
            else:
                if max_result < result:
                    max_result = result
print(max_result)