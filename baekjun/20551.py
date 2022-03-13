def binary_search(n):
    start = 0
    end = N - 1

    while start <= end:
        mid = (start + end) // 2
        if nums[mid] > n:
            end = mid - 1
        elif nums[mid] < n:
            start = mid + 1
        else:
            if end == mid:
                break
            end = mid
    if nums[mid] == n:
        return mid
    else: return -1


import sys

input = sys.stdin.readline

N, M = map(int, input().split())
nums = []

for _ in range(N):
    nums.append(int(input()))

nums.sort()

for _ in range(M):
    num = int(input())
    idx = binary_search(num)
    print(idx)