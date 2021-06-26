N = int(input())

nums = list(map(int, input().split()))
result = [0] * N

nums_sort = list(sorted(set(nums)))
dic = {nums_sort[i]:i for i in range(len(nums_sort))}

for num in nums:
    print(dic[num], end=' ')