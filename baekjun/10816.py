N = int(input())
cards = list(map(int, input().split()))
M = int(input())
nums = list(map(int, input().split()))
sorted_nums = sorted(nums)

cards.sort()

idx = 0
result = {}

for num in sorted_nums:
    cnt = 0
    if num not in result:
        while idx < len(cards):
            if num == cards[idx]:
                cnt += 1
                idx += 1
            elif num > cards[idx]:
                idx += 1
            else:
                break
        result[num] = cnt

for num in nums:
    print(result[num], end=" ")