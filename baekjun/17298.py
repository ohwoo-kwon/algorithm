n = int(input())
nums = list(map(int, input().split()))
stack = [0]
result = [-1 for _ in range(n)]


i = 1
while stack and i<n:
    while stack and nums[stack[-1]] < nums[i]:
        result[stack[-1]] = nums[i]
        stack.pop()

    stack.append(i)
    i += 1

print(*result)