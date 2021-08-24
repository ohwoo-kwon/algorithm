N = int(input())
nums = [i for i in range(1, N+1)] + [0] * 10000000
f = 0
r = N - 1

while f != r:
    f += 1
    r += 1
    nums[r] = nums[f]
    f += 1

print(nums[f])