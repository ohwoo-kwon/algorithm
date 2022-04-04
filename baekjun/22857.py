N, K = map(int, input().split())
nums = list(map(int, input().split()))
answer = 0

for i in range(N):
    cnt = 1
    remain = K
    if nums[i] % 2 or (i != 0 and nums[i-1] % 2 == 0):
        continue
    for j in range(i+1, N):
        if remain == 0:
            while j < N and nums[j] % 2 == 0:
                j += 1
                cnt += 1
            answer = max(cnt, answer)
            break
        if nums[j] % 2:
            remain -= 1
        else:
            cnt += 1
    else:
        answer = max(cnt, answer)

print(answer)