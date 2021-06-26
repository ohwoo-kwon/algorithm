N = int(input())
nums = [int(input()) for _ in range(N)]

nums = sorted(nums)

for i in range(N):
    print(nums[i])