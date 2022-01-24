def Perm(i, sum_temp, N, M):
    if sum_temp > M:
        return
    if i >= 3:
        global sum_nums
        sum_nums = max(sum_nums, sum_temp)
        return
    for j in range(N):
        if not visited[j]:
            sum_temp += cards[j]
            visited[j] = True
            Perm(i+1, sum_temp, N, M)
            sum_temp -= cards[j]
            visited[j] = False




N, M = map(int, input().split())
cards = list(map(int, input().split()))
visited = [False] * N
sum_nums = 0

Perm(0, sum_nums, N, M)
print(sum_nums)