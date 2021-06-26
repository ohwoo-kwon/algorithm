N = int(input())
nums = list(map(int, input().split()))

cnt = 0

for i in range(N):
    if nums[i] < 0:
        cnt += nums[i]
    else:
        cnt += nums[i]
    nums[i] = cnt
    if cnt < 0:
        cnt = 0
print(max(nums))